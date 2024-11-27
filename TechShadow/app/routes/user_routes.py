from flask import request, jsonify, Blueprint
from app.queries.user_queries import get_users, get_user, create_user, update_user, delete_user

user_bp = Blueprint("users", __name__)


@user_bp.route("/users")
def get_all_users():
    try:
        users = get_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch users"}), 500


@user_bp.route("/user", methods=["POST"])
def post_user():
    try:
        data = request.get_json()
        user = create_user(data)
        return jsonify(user), 201
    except RuntimeError as e:
        return jsonify({f"error: {e}"})


@user_bp.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def get_one_user(user_id):
    if request.method == "GET":
        try:
            user = get_user(user_id)
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": "User not found"}), 404
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "PUT":
        try:
            data = request.get_json()
            user = update_user(user_id, data)
            return jsonify(user), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            user = delete_user(user_id)
            return jsonify(user), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
