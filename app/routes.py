
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import os
import psycopg
from flask import jsonify
import stripe
from flask import url_for

main = Blueprint("main", __name__)

# =========================
# POSTGRES CONNECTION
# =========================

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL *****:")
print(DATABASE_URL)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

DOMAIN = os.getenv("DOMAIN")
PRICE_IDS = {
    "pro": "price_1TZyHoIRwgjrfptjJ0SZLeIS"
}

def get_connection():
    return psycopg.connect(DATABASE_URL)

# =========================
# HOME
# =========================

@main.route("/")
def home():
 return render_template("home.html")
 

# =========================
# REGISTER
# =========================

@main.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(name,email,password_hash)
            VALUES(%s,%s,%s)
            """,
            (name, email, hashed_password)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

# =========================
# LOGIN
# =========================

@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT id, name, password_hash
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:

            user_id = user[0]
            name = user[1]
            password_hash = user[2]

            if check_password_hash(password_hash, password):

                session["user_id"] = user_id
                session["user"] = name
                session["email"] = email

                return redirect("/dashboard")

    return render_template("login.html")

# =========================
# LOGOUT
# =========================

@main.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@main.route("/dashboard")
def dashboard():

    # =========================
    # VALIDAR LOGIN
    # =========================

    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    user = session.get("user")

    # =========================
    # CONEXIÓN DB
    # =========================

    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # VALIDAR SUSCRIPCIÓN
    # =========================

    cursor.execute(
        """
        SELECT active, plan_name
        FROM subscriptions
        WHERE user_id = %s
        AND active = TRUE
        ORDER BY created_at DESC
        LIMIT 1
        """,
        (user_id,)
    )

    subscription = cursor.fetchone()

    has_subscription = False
    plan_name = None

    if subscription:

        has_subscription = subscription[0]
        plan_name = subscription[1]

    # =========================
    # TOTAL CURSOS
    # =========================

    total_courses = 3

    # =========================
    # PROGRESO GENERAL
    # =========================

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM course_progress
        WHERE user_id = %s
        """,
        (user_id,)
    )

    completed_modules = cursor.fetchone()[0]

    total_modules = 12

    progress_percent = int(
        (completed_modules / total_modules) * 100
    ) if total_modules > 0 else 0

    cursor.close()
    conn.close()

    # =========================
    # RENDER TEMPLATE
    # =========================

    return render_template(
        "dashboard.html",
        user=user,
        has_subscription=has_subscription,
        plan_name=plan_name,
        progress_percent=progress_percent,
        total_courses=total_courses
    )


@main.route("/course/databricks")
def databricks_course():

    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT active
        FROM subscriptions
        WHERE user_id = %s
        AND active = TRUE
        """,
        (user_id,)
    )

    subscription = cursor.fetchone()

    cursor.close()
    conn.close()

    if not subscription:
        return redirect("/dashboard")

    return render_template("databricks.html")


@main.route("/course/ml-engineer")
def ml_engineer_course():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("ml_engineer.html")


@main.route("/course/mlops")
def mlops_course():

    if "user_id" not in session:
        return redirect("/login")

    return render_template("mlops.html")

@main.route("/save-progress", methods=["POST"])
def save_progress():

    if "user_id" not in session:
        return jsonify({"success": False})

    data = request.get_json()

    module_id = data["module_id"]
    course_name = data["course_name"]

    user_id = session["user_id"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM course_progress
        WHERE user_id = %s
        AND course_name = %s
        AND module_id = %s
        """,
        (user_id, course_name, module_id)
    )

    existing = cursor.fetchone()

    if not existing:

        cursor.execute(
            """
            INSERT INTO course_progress (
                user_id,
                course_name,
                module_id,
                completed
            )
            VALUES (%s, %s, %s, TRUE)
            """,
            (user_id, course_name, module_id)
        )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"success": True})

@main.route("/get-progress/<course_name>")
def get_progress(course_name):

    if "user_id" not in session:
        return jsonify([])

    user_id = session["user_id"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT module_id
        FROM course_progress
        WHERE user_id = %s
        AND course_name = %s
        """,
        (user_id, course_name)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    completed_modules = [row[0] for row in rows]

    return jsonify(completed_modules)

@main.route("/webhook", methods=["POST"])
def stripe_webhook():

    payload = request.data

    sig_header = request.headers.get("Stripe-Signature")

    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:

        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            webhook_secret
        )

    except Exception as e:
        return str(e), 400

    # =========================
    # CHECKOUT COMPLETED
    # =========================

    if event["type"] == "checkout.session.completed":

        session_data = event["data"]["object"]

        customer_email = session_data["customer_details"]["email"]

        stripe_session_id = session_data["id"]

        conn = get_connection()
        cursor = conn.cursor()

        # buscar usuario
        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE email = %s
            """,
            (customer_email,)
        )

        user = cursor.fetchone()

        if user:

            user_id = user[0]

            cursor.execute(
                """
                INSERT INTO subscriptions(
                    user_id,
                    stripe_session_id,
                    plan_name,
                    active
                )
                VALUES(%s,%s,%s,TRUE)
                """,
                (
                    user_id,
                    stripe_session_id,
                    "pro"
                )
            )

            conn.commit()

        cursor.close()
        conn.close()

    return "", 200


@main.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():

    if "user_id" not in session:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    data = request.get_json()

    plan = data.get("plan")

    try:

        checkout_session = stripe.checkout.Session.create(

            payment_method_types=["card"],

            line_items=[
                {
                    "price": PRICE_IDS[plan],
                    "quantity": 1,
                }
            ],

            mode="subscription",

            success_url=DOMAIN + "/success",

            cancel_url=DOMAIN + "/cancel",

            customer_email=session.get("email")

        )

        return jsonify({
            "url": checkout_session.url
        })

    except Exception as e:

        print("STRIPE ERROR:")
        print(str(e))

        return jsonify({
            "error": str(e)
        }), 500
  
@main.route("/success")
def success():

    return render_template("success.html")


@main.route("/cancel")
def cancel():

    return "Pago cancelado"