'''Implements database access/posting methods for shadows page.'''
from flask import request, render_template, Blueprint, jsonify
from queries.shadow_queries import get_shadows, get_shadow, create_shadow, update_shadow, delete_shadow

shadow_bp = Blueprint("shadows", __name__)


@shadow_bp.route('/shadows', methods=["GET"])
def shadow():
    try:
        shadows = get_shadows()
        return render_template('shadows.html', shadows=shadows), 200
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

@shadow_bp.route("/shadow", methods=["POST"])
def post_shadow():
    try:
        data = request.get_json()
        shadow = create_shadow(data)
        return jsonify(shadow), 201
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

@shadow_bp.route("/shadow/<int:shadow_id>", methods=["GET", "PUT", "DELETE"])
def get_one_shadow(shadow_id):
    if request.method == "GET":
        try:
            shadow = get_shadow(shadow_id)
            return jsonify(shadow)
        except ValueError:
            return jsonify({"error": "Shadow not found"})
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "PUT":
        try:
            data = request.get_json()
            shadow = update_shadow(data, shadow_id)
            return jsonify(shadow), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            shadow = delete_shadow(shadow_id)
            return jsonify(shadow), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
