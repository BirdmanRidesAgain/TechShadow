'''Implements database access/posting methods for messages page.'''
from flask import request, Blueprint, jsonify
from queries.message_queries import get_messages, get_message, create_message, update_message, delete_message, get_messages_by_user

message_bp = Blueprint("messages", __name__)


@message_bp.route("/messages")
def get_all_messages():
    try:
        messages = get_messages()
        return jsonify(messages), 200
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

# TODO implement this for admin review of messages
@message_bp.route("/messages/<user_id>", methods=["GET"])
def get_messages_by_userid(user_id):
    try:
        messages = get_messages_by_user(user_id)
        return jsonify(messages), 200
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

@message_bp.route("/message", methods=["POST"])
def post_message():
    try:
        data = request.get_json()
        message = create_message(data)
        return jsonify(message), 201
    except RuntimeError as e:
            return jsonify({"error": str(e)}), 500


@message_bp.route("/message/<int:message_id>", methods=["GET", "PUT", "DELETE"])
def get_one_message(message_id):
    if request.method == "GET":
        try:
            message = get_message(message_id)
            return jsonify(message), 200
        except ValueError:
            return jsonify({"error": "Message not found"})
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "PUT":
        try:
            data = request.get_json()
            message = update_message(message_id, data)
            return jsonify(message), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == "DELETE":
        try:
            message = delete_message(message_id)
            return jsonify(message), 200
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 500
