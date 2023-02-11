from flask import Blueprint
from model.user import User
from schema.users_schema import user_schema, users_schema

user = Blueprint('user', __name__, url_prefix="/users")

@user.get("/")
def get_users():
    users = User.query.all()
    return user_schema.dump(users)

