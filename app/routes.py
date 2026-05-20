from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return {
        "message": "Hello World from Flask on DigitalOcean 🚀"
    }