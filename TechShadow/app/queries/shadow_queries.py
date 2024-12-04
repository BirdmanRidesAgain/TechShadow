import psycopg2
from tsdb import create_connection
from flask import jsonify


def get_shadows():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT position, job_description, status, location, userID FROM Opportunities;")
            rows = cur.fetchall()
            opportunities = []
            for row in rows:
                opportunity = {
                    'position': row[0],
                    'job_description': row[1],
                    'status': row[2],
                    'location': row[3],
                    'userID': row[4]
                }
                opportunities.append(opportunity)
            return opportunities
    except Exception as e:
        raise RuntimeError(f"Failed to fetch shadows from database: {e}")
    finally:
        if conn:
            conn.close()


# TODO integrate this into shadow list page as filter
def get_shadows_by_username(username):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                        SELECT
                        opportunities.position,
                        opportunities.job_description,
                        opportunities.status,
                        opportunities.location
                        FROM Opportunities
                        JOIN Users ON opportunities.userID = Users.userID
                        WHERE Users.username = %s;
                        """, (username,))
            rows = cur.fetchall()
            opportunities = []
            for row in rows:
                opportunity = {
                    'position': row[0],
                    'job_description': row[1],
                    'status': row[2],
                    'location': row[3]
                }
                opportunities.append(opportunity)
            return opportunities
    except Exception as e:
        raise RuntimeError(f"Failed to fetch shadows for this username: {e}")
    finally:
        if conn:
            conn.close()


def get_shadow(shadow_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                opportunityID,
                position,
                job_description,
                status,
                location,
                userID
                FROM Opportunities
                WHERE opportunityID = %s;
                """, (shadow_id,))
            row = cur.fetchone()
            if row:
                shadow = {
                    "opportunityID": row[0],
                    "position": row[1],
                    "job_description": row[2],
                    "status": row[3],
                    "location": row[4],
                    "userID": row[5]
                }
                return shadow
            else:
                raise ValueError("shadow not found")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch shadow from database: {e}")
    finally:
        if conn:
            conn.close()


def create_shadow(data):
    position = data.get("position")
    job_description = data.get("job_description")
    is_remote = data.get("is_remote")
    is_in_person = data.get("is_in_person")
    status = data.get("status")
    required_skills = data.get("required_skills")
    location = data.get("location")
    # TODO: update when users can login and userID can be automatically passed
    userID = 1

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO opportunities (
                position,
                job_description,
                is_remote,
                is_in_person,
                status,
                required_skills,
                location,
                userID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING opportunityID;
                """,
                (position,
                 job_description,
                 is_remote,
                 is_in_person,
                 status,
                 required_skills,
                 location,
                 userID)
            )
            shadow_id = cur.fetchone()[0]
            conn.commit()
            return {
                "messsage": f"shadow {shadow_id} created",
                "shadowID": shadow_id
                }
    except Exception as e:
        raise RuntimeError(f"Error creating shadow: {e}")
    finally:
        if conn:
            conn.close()


def update_shadow(data, shadow_id):

    position = data.get("position")
    job_description = data.get("job_description")
    is_remote = data.get("is_remote")
    is_in_person = data.get("is_in_person")
    status = data.get("status")
    required_skills = data.get("required_skills")
    location = data.get("location")

    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE opportunities
                SET position = %s,
                job_description = %s,
                is_remote = %s,
                is_in_person = %s,
                status = %s,
                required_skills = %s,
                location = %s
                WHERE opportunityID = %s;
                """,
                (position,
                 job_description,
                 is_remote,
                 is_in_person,
                 status,
                 required_skills,
                 location,
                 shadow_id)
            )
            conn.commit()
            return {
                "message": f"shadow {shadow_id} updated",
                "shadowID": shadow_id
                }
    except Exception as e:
        raise RuntimeError(f"Error updating shadow: {e}")
    finally:
        if conn:
            conn.close()


def delete_shadow(shadow_id):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM opportunities WHERE opportunityID = %s;", (shadow_id,))
            conn.commit()
            return {
                "message": f"shadow {shadow_id} deleted",
                "shadowID": shadow_id
                }
    except Exception as e:
        raise RuntimeError(f"Error deleting shadow: {e}")
    finally:
        if conn:
            conn.close()
