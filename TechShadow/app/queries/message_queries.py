from tsdb import create_connection
from flask import jsonify


def get_messages():
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM messages;")
            rows = cur.fetchall()
            return rows
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def get_message(message_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM messages WHERE messageID = %s;
                """, (message_id,))
            message = cur.fetchone()
            if message:
                message_json = {
                    "messageID": message[0],
                    "userID": message[1],
                    "message_content": message[2],
                    "created_at": message[3],
                    "userID2": message[4],
                    "responded_at": message[5],
                    "status": message[6]
                }
                return jsonify(message_json)
            else:
                return jsonify({"error": "message not found"})
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def create_message(data):
    userID = data.get("userID")
    message_content = data.get("message_content")
    userID2 = data.get("userID2")
    status = data.get("status")

    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO messages (userID, message_content, userID2, status)
                VALUES (%s, %s, %s, %s)
                RETURNING messageID;
                """,
                (userID, message_content, userID2, status)
            )
            message_id = cur.fetchone()[0]
            conn.commit()
            print(f"Successfully created message {message_id}")
            return jsonify({"message_id": message_id})
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()


def update_message(message_id, data):

    message_content = data.get("message_content")
    status = data.get("status")

    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE messages
                SET message_content = %s, status = %s
                WHERE messageID = %s;
                """,
                (message_content, status, message_id)
            )
            conn.commit()
            return f"Successfully updated message {message_id}"
    except Exception as e:
        return f"error: {e}"
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
            return jsonify({"message": f"Message {message_id} deleted"})
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()
