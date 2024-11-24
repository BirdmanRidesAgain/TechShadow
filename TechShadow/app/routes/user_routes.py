from flask import request, jsonify, Blueprint
from queries.user_queries import get_users, get_user, create_user, update_user, delete_user

user_bp = Blueprint("users", __name__)


@user_bp.route("/users")
def get_all_users():
    return get_users()


@user_bp.route("/user", methods=["POST"])
def post_user():
    data = request.get_json()
    return create_user(data)


@user_bp.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def get_one_user(user_id):
    if request.method == "GET":
        return get_user(user_id)
    elif request.method == "PUT":
        data = request.get_json()
        return update_user(user_id, data)

    elif request.method == "DELETE":
        return delete_user(user_id)
