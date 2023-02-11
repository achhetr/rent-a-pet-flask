from flask import Blueprint

home = Blueprint('home', __name__, url_prefix="/home")

@home.get("/index")
def get_home_page():
    return { "message": "George is great!"}

