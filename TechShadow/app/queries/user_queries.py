from tsdb import create_connection

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
            cur.execute("SELECT * FROM Users WHERE userID = %s;", (user_id))
            user = cur.fetchone()
            if user:
                return user
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def create_user():
    return "this creates a user"


def update_user(user_id):
    return f"this updates the user with ID {user_id}"


def delete_user(user_id):
    return f"this deletes the user with ID {user_id}"
