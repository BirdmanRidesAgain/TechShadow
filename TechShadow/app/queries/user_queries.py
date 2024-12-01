from tsdb import create_connection
from flask import jsonify

# add queries for user table here


def get_users():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users;")
            rows = cur.fetchall()
            if rows:
                users = [{
                    "userID": row[0],
                    "username": row[1],
                    "first_name": row[3],
                    "last_name": row[4],
                    "is_mentor": row[5],
                    "is_shadower": row[6],
                    "field": row[7],
                    "email": row[8]
                } for row in rows]
                return users
    except Exception as e:
        raise RuntimeError(f"Failed to fetch users from database: {e}")
    finally:
        if conn:
            conn.close()


def get_user(user_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM Users WHERE userID = %s;", (user_id,))
            row = cur.fetchone()
            if row:
                user = {
                    "userID": row[0],
                    "username": row[1],
                    "first_name": row[3],
                    "last_name": row[4],
                    "is_mentor": row[5],
                    "is_shadower": row[6],
                    "field": row[7],
                    "email": row[8]
                }
                return user
            else:
                raise ValueError("User not found")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch user from database: {e}")
    finally:
        if conn:
            conn.close()


def create_user(data):
    username = data.get("username")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    is_mentor = data.get("is_mentor")
    is_shadower = data.get("is_shadower")
    field = data.get("field")
    email = data.get("email")

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (username, password, first_name, last_name, is_mentor, is_shadower, field, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING userID;
                """,
                (username,
                 password,
                 first_name,
                 last_name,
                 is_mentor,
                 is_shadower,
                 field,
                 email)
            )
            user_id = cur.fetchone()[0]
            conn.commit()
            return {"message": f"User {user_id} created", "userID": user_id}
    except Exception as e:
        raise RuntimeError(f"Error creating user: {e}")
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
    email = data.get("email")

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE users
                SET username = %s, password = %s, first_name = %s, last_name = %s, is_mentor = %s, is_shadower = %s, field = %s, email = %s
                WHERE userID = %s;
                """,
                (username,
                 password,
                 first_name,
                 last_name,
                 is_mentor,
                 is_shadower,
                 field,
                 email,
                 user_id)
            )
            conn.commit()
            return {"message": f"User {user_id} updated", "userID": user_id}
    except Exception as e:
        raise RuntimeError(f"Error updating user: {e}")
    finally:
        if conn:
            conn.close()


def delete_user(user_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE userID = %s;", (user_id,))
            conn.commit()
            return {"message": f"User {user_id} deleted", "userID": user_id}
    except Exception as e:
        raise RuntimeError(f"Error deleting user: {e}")
    finally:
        if conn:
            conn.close()
