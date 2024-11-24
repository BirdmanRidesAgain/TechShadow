from flask import request, render_template, Blueprint
from queries.shadow_queries import get_shadows, get_shadow, create_shadow, update_shadow, delete_shadow

shadow_bp = Blueprint("shadows", __name__)

@shadow_bp.route('/shadows', methods=["GET"])
def shadow():
    shadows = get_shadows()
    return shadows
    # return render_template('shadows.html', shadows=shadows)


@shadow_bp.route("/shadow", methods=["POST"])
def post_shadow():
    data = request.get_json()
    return create_shadow(data)


@shadow_bp.route("/shadow/<int:shadow_id>", methods=["GET", "PUT", "DELETE"])
def get_one_shadow(shadow_id):
    if request.method == "GET":
        return get_shadow(shadow_id)
    elif request.method == "PUT":
        data = request.get_json()
        return update_shadow(data, shadow_id)
    elif request.method == "DELETE":
        return delete_shadow(shadow_id)
