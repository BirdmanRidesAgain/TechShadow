'''Implements functions for handling/relaying methods to and from the database.'''
from tsdb import create_connection


def get_messages():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM messages;")
            rows = cur.fetchall()
            if rows:
                messages = [{
                    "messageID": row[0],
                    "name": row[1],
                    "email": row[2],
                    "message_content": row[3],
                    "userID": row[4],
                } for row in rows]
                return messages
    except Exception as e:
        raise RuntimeError(f"Failed to fetch messages from database: {e}")
    finally:
        if conn:
            conn.close()


# TODO: integrate this for admins to see messages by users
def get_messages_by_user(user_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT
                        messages.name,
                        messages.email,
                        messages.message_content
                        FROM Messages
                        WHERE Messages.userID = %s;
                        """, (user_id,))
            rows = cur.fetchall()
            messages = []
            for row in rows:
                message = {
                    "name": row[0],
                    "email": row[1],
                    "message_content": row[2]
                }
                messages.append(message)
            return messages
    except Exception as e:
        raise RuntimeError(f"Failed to fetch messages for this userID: {e}")
    finally:
        if conn:
            conn.close()


def get_message(message_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM messages WHERE messageID = %s;
                """, (message_id,))
            row = cur.fetchone()
            if row:
                message = {
                    "messageID": row[0],
                    "name": row[1],
                    "email": row[2],
                    "message_content": row[3],
                    "userID": row[4]
                }
                return message
            else:
                raise ValueError("message not found")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch message from database: {e}")
    finally:
        if conn:
            conn.close()


def create_message(data):
    name = data.get("name")
    email = data.get("email")
    message_content = data.get("message_content")
    # TODO: update when users are able to login and pass this automatically
    userID = 1
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO messages (name, email, message_content, userID)
                VALUES (%s, %s, %s, %s)
                RETURNING messageID;
                """,
                (name, email, message_content, userID)
            )
            message_id = cur.fetchone()[0]
            conn.commit()
            return {
                "message": f"Message {message_id} created",
                "messageID": message_id
                }
    except Exception as e:
        raise RuntimeError(f"Error creating message: {e}")
    finally:
        if conn:
            conn.close()


def update_message(message_id, data):
    name = data.get("name")
    email = data.get("email")
    message_content = data.get("message_content")

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE messages
                SET name = %s, email = %s, message_content = %s
                WHERE messageID = %s;
                """,
                (name, email, message_content, message_id)
            )
            conn.commit()
            return {
                "message": f"Message {message_id} updated",
                "messageID": message_id
                }
    except Exception as e:
        raise RuntimeError(f"Error updating message: {e}")
    finally:
        if conn:
            conn.close()


def delete_message(message_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM messages WHERE messageID = %s;
                """, (message_id,))
            conn.commit()
            return {
                "message": f"Message {message_id} deleted",
                "messageID": message_id
                }
    except Exception as e:
        raise RuntimeError(f"Error deleting message: {e}")
    finally:
        if conn:
            conn.close()
