from tsdb import create_connection
from flask import jsonify

# add queries for user table here

def get_users():
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users;")
            rows = cur.fetchall()
            return rows
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def get_user(user_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users WHERE userID = %s;", (user_id,))
            user = cur.fetchone()
            if user:
                user_json = {
                    "userID": user[0],
                    "username": user[1],
                    "first_name": user[3],
                    "last_name": user[4],
                    "is_mentor": user[5],
                    "is_shadower": user[6],
                    "field": user[7]
                }
                return jsonify(user_json)
            else:
                return jsonify({"error": "User not found"})
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def create_user(data):
    username = data.get("username")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    is_mentor = data.get("is_mentor")
    is_shadower = data.get("is_shadower")
    field = data.get("field")

    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (username, password, first_name, last_name, is_mentor, is_shadower, field)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """,
                (username, password, first_name, last_name, is_mentor, is_shadower, field)
            )
            conn.commit()
            return f"Successfully created user {username}"
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()


def update_user(user_id, data):

    username = data.get("username")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    is_mentor = data.get("is_mentor")
    is_shadower = data.get("is_shadower")
    field = data.get("field")

    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE users
                SET username = %s, password = %s, first_name = %s, last_name = %s, is_mentor = %s, is_shadower = %s, field = %s
                WHERE userID = %s;
                """,
                (username, password, first_name, last_name, is_mentor, is_shadower, field, user_id)
            )
            conn.commit()
            return f"Successfully updated user {first_name} {last_name}"
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()


def delete_user(user_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE userID = %s;", (user_id,))
            conn.commit()
            return jsonify({"message": f"User {user_id} deleted"})
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()
