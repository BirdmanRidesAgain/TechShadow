from ts_app import app
from queries.message_queries import get_messages, get_message, create_message, update_message, remove_message


@app.route("/messages")
def get_all_messages():
    return get_messages()


@app.route("/message/<int:message_id>")
def get_one_message(message_id):
    return get_message(message_id)


@app.route("/message")
def post_message(message_id):
    return create_message(message_id)


@app.route("/update_message/<int:message_id>")
def put_message(message_id):
    return update_message(message_id)


@app.route("/remove_message/<int:message_id>")
def delete_message(message_id):
    return remove_message(message_id)
