from flask import request
from ts_app import app
from queries.message_queries import get_messages, get_message, create_message, update_message, delete_message


@app.route("/messages")
def get_all_messages():
    return get_messages()


@app.route("/message", methods=["POST"])
def post_message():
    data = request.get_json()
    return create_message(data)


@app.route("/message/<int:message_id>", methods=["GET", "PUT", "DELETE"])
def get_one_message(message_id):
    if request.method == "GET":
        return get_message(message_id)
    elif request.method == "PUT":
        data = request.get_json()
        return update_message(message_id, data)
    elif request.method == "DELETE":
        return delete_message(message_id)
