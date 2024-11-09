from ts_app import app
from queries.user_queries import get_users, get_user, create_user, update_user, remove_user


@app.route("/users")
def get_all_users():
    return get_users()


@app.route("/user/<int:user_id>")
def get_one_user(user_id):
    return get_user(user_id)


@app.route("/user")
def post_user(user_id):
    return create_user(user_id)


@app.route("/update_user/<int:user_id>")
def put_user(user_id):
    return update_user(user_id)


@app.route("/remove_user/<int:user_id>")
def delete_user(user_id):
    return remove_user(user_id)
