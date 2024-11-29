from tsdb import create_connection
from flask import jsonify


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
                    "message_content": row[3]
                } for row in rows]
                return messages
    except Exception as e:
        raise RuntimeError(f"Failed to fetch messages from database: {e}")
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
                }
                return message
            else:
                raise ValueError("message not found")
    except Exception as e:
        return RuntimeError(f"Failed to fetch message from database: {e}")
    finally:
        if conn:
            conn.close()


def create_message(data):
    name = data.get("name")
    email = data.get("email")
    message_content = data.get("message_content")

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO messages (name, email, message_content)
                VALUES (%s, %s, %s)
                RETURNING messageID;
                """,
                (name, email, message_content)
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
