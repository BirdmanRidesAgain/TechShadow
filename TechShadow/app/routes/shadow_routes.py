from ts_app import app
from queries.shadow_queries import get_shadows, get_shadow, create_shadow, update_shadow, remove_shadow


@app.route("/shadows")
def get_all_shadows():
    return get_shadows()


@app.route("/shadow/<int:shadow_id>")
def get_one_shadow(shadow_id):
    return get_shadow(shadow_id)


@app.route("/shadow")
def post_shadow(shadow_id):
    return create_shadow(shadow_id)


@app.route("/update_shadow/<int:shadow_id>")
def put_shadow(shadow_id):
    return update_shadow(shadow_id)


@app.route("/remove_shadow/<int:shadow_id>")
def delete_shadow(shadow_id):
    return remove_shadow(shadow_id)
