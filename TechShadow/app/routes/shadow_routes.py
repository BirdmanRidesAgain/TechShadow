from flask import request
from ts_app import app
from queries.shadow_queries import get_shadows, get_shadow, create_shadow, update_shadow, delete_shadow


@app.route("/shadows")
def get_all_shadows():
    return get_shadows()


@app.route("/shadow", methods=["POST"])
def post_shadow():
    return create_shadow()


@app.route("/shadow/<int:shadow_id>", methods=["GET", "PUT", "DELETE"])
def get_one_shadow(shadow_id):
    if request.method == "GET":
        return get_shadow(shadow_id)
    elif request.method == "PUT":
        return update_shadow(shadow_id)
    elif request.method == "DELETE":
        return delete_shadow(shadow_id)
