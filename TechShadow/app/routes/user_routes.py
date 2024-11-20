from flask import request
from ts_app import app
from queries.user_queries import get_users, get_user, create_user, update_user, delete_user


@app.route("/users")
def get_all_users():
    return get_users()

@app.route("/user", methods=["POST"])
def post_user():
    return create_user()


@app.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def get_one_user(user_id):
    if request.method == "GET":
        return get_user(user_id)
    elif request.method == "PUT":
        return update_user(user_id)
    elif request.method == "DELETE":
        return delete_user(user_id)
