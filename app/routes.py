from flask import Blueprint, render_template_string, request, redirect, session
import psycopg
import os
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

# =========================
# POSTGRES CONNECTION
# =========================

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL *****:")
print(DATABASE_URL)

def get_connection():
    return psycopg.connect(DATABASE_URL)

# =========================
# HOME
# =========================

@main.route("/")
def home():

    user = session.get("user")

    html = f"""

<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Meteora IA</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

*{{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body{{
    font-family:'Inter',sans-serif;
    background:#020617;
    color:white;
}}

header{{
    position:fixed;
    top:0;
    width:100%;
    background:rgba(2,6,23,0.92);
    backdrop-filter:blur(10px);
    border-bottom:1px solid rgba(255,255,255,0.06);
    z-index:1000;
}}

.nav{{
    max-width:1300px;
    margin:auto;
    padding:20px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

.logo{{
    font-size:30px;
    font-weight:800;
    background:linear-gradient(to right,#38bdf8,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

nav{{
    display:flex;
    align-items:center;
    gap:30px;
}}

nav a{{
    text-decoration:none;
    color:#cbd5e1;
}}

.auth{{
    display:flex;
    gap:15px;
}}

.login{{
    padding:10px 20px;
    border:1px solid rgba(255,255,255,0.12);
    border-radius:12px;
    color:white;
    text-decoration:none;
}}

.register{{
    padding:10px 20px;
    border-radius:12px;
    background:linear-gradient(to right,#38bdf8,#8b5cf6);
    color:white;
    text-decoration:none;
    font-weight:600;
}}

.hero{{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:120px 40px;
}}

.hero-content{{
    max-width:900px;
}}

.hero h1{{
    font-size:72px;
    line-height:1.1;
    margin-bottom:30px;
}}

.gradient{{
    background:linear-gradient(to right,#38bdf8,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

.hero p{{
    font-size:20px;
    color:#cbd5e1;
    line-height:1.8;
}}

.button{{
    margin-top:40px;
    display:inline-block;
    padding:16px 30px;
    border-radius:14px;
    background:linear-gradient(to right,#38bdf8,#8b5cf6);
    text-decoration:none;
    color:white;
    font-weight:600;
}}

.welcome{{
    color:#38bdf8;
    font-weight:600;
}}

</style>

</head>

<body>

<header>

<div class="nav">

<div class="logo">
Meteora IA
</div>

<nav>

<a href="#">Capacitaciones</a>
<a href="#">Meteora</a>
<a href="#">Carlos Nieblas</a>

<div class="auth">
"""

    if user:

        html += f"""
        <span class="welcome">
            Hola {user}
        </span>

        <a href="/logout" class="login">
            Logout
        </a>
        """

    else:

        html += """
        <a href="/login" class="login">
            Iniciar Sesión
        </a>

        <a href="/register" class="register">
            Crear Cuenta
        </a>
        """

    html += """

</div>

</nav>

</div>

</header>

<section class="hero">

<div class="hero-content">

<h1>
Domina
<span class="gradient">
AI, Databricks y MLOps
</span>
</h1>

<p>
Capacitación profesional para ingenieros y científicos de datos
que buscan construir soluciones empresariales modernas.
</p>

<a class="button" href="#">
Explorar Programas
</a>

</div>

</section>

</body>
</html>

"""

    return render_template_string(html)

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

    return render_template_string("""

    <html>

    <head>

    <title>Registro</title>

    <style>

    body{
        background:#020617;
        font-family:Arial;
        color:white;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }

    .card{
        background:#0f172a;
        padding:40px;
        border-radius:20px;
        width:400px;
    }

    input{
        width:100%;
        padding:14px;
        margin-top:15px;
        border:none;
        border-radius:10px;
        background:#1e293b;
        color:white;
    }

    button{
        width:100%;
        margin-top:20px;
        padding:14px;
        border:none;
        border-radius:10px;
        background:linear-gradient(to right,#38bdf8,#8b5cf6);
        color:white;
        font-weight:bold;
    }

    </style>

    </head>

    <body>

    <form method="POST" class="card">

        <h1>Crear Cuenta</h1>

        <input type="text" name="name" placeholder="Nombre" required>

        <input type="email" name="email" placeholder="Correo" required>

        <input type="password" name="password" placeholder="Contraseña" required>

        <button type="submit">
            Registrarse
        </button>

    </form>

    </body>

    </html>

    """)

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
            SELECT id,name,password_hash
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

                return redirect("/")

    return render_template_string("""

    <html>

    <head>

    <title>Login</title>

    <style>

    body{
        background:#020617;
        font-family:Arial;
        color:white;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }

    .card{
        background:#0f172a;
        padding:40px;
        border-radius:20px;
        width:400px;
    }

    input{
        width:100%;
        padding:14px;
        margin-top:15px;
        border:none;
        border-radius:10px;
        background:#1e293b;
        color:white;
    }

    button{
        width:100%;
        margin-top:20px;
        padding:14px;
        border:none;
        border-radius:10px;
        background:linear-gradient(to right,#38bdf8,#8b5cf6);
        color:white;
        font-weight:bold;
    }

    </style>

    </head>

    <body>

    <form method="POST" class="card">

        <h1>Iniciar Sesión</h1>

        <input type="email" name="email" placeholder="Correo" required>

        <input type="password" name="password" placeholder="Contraseña" required>

        <button type="submit">
            Entrar
        </button>

    </form>

    </body>

    </html>

    """)

# =========================
# LOGOUT
# =========================

@main.route("/logout")
def logout():

    session.clear()

    return redirect("/")