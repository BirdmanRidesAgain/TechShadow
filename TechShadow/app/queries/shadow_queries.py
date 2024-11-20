import psycopg2
from tsdb import create_connection
from flask import jsonify


def get_shadows():
    conn = create_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT position, job_description, status, location FROM Opportunities;")
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
            print(f"An error occurred while fetching opportunities: {e}")
        finally:
            conn.close()
    else:
        return []


def get_shadow(shadow_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM opportunities WHERE opportunityID = %s;
                """, (shadow_id,))
            shadow = cur.fetchone()
            if shadow:
                shadow_json = {
                    "opportunityID": shadow[0],
                    "position": shadow[1],
                    "job_description": shadow[2],
                    "is_remote": shadow[3],
                    "is_in_person": shadow[4],
                    "status": shadow[5],
                    "required_skills": shadow[6],
                    "location": shadow[7]
                }
                return jsonify(shadow_json)
            else:
                return jsonify({"error": "shadow not found"})
    except Exception as e:
        return f"error: {e}"
    finally:
        conn.close()


def create_shadow(data):
    position = data.get("position")
    job_description = data.get("job_description")
    is_remote = data.get("is_remote")
    is_in_person = data.get("is_in_person")
    status = data.get("status")
    required_skills = data.get("required_skills")
    location = data.get("location")

    conn = create_connection()
    try:
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
                location)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING opportunityID;
                """,
                (position,
                 job_description,
                 is_remote,
                 is_in_person,
                 status,
                 required_skills,
                 location)
            )
            shadow_id = cur.fetchone()[0]
            conn.commit()
            print(f"Successfully created shadow {shadow_id}")
            return jsonify({"shadowID": shadow_id})
    except Exception as e:
        return f"error: {e}"
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

    conn = create_connection()
    try:
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
            return f"Successfully updated shadow {shadow_id}"
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()


def delete_shadow(shadow_id):
    conn = create_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM opportunities WHERE opportunityID = %s;", (shadow_id,))
            conn.commit()
            return jsonify({"message": f"shadow {shadow_id} deleted"})
    except Exception as e:
        return f"error: {e}"
    finally:
        if conn:
            conn.close()
