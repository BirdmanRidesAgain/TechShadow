# add queries for message table here

def get_messages():
    return "List of all messages"


def get_message(message_id):
    return f"this is the message with ID {message_id}"


def create_message():
    return f"this creates a message"


def update_message(message_id):
    return f"this updates the message with ID {message_id}"


def remove_message(message_id):
    return f"this deletes the message with ID {message_id}"
