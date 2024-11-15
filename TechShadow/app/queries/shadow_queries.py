import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="techshadowdb",
            user="techshadowdb_user",
            password="tftK4LBskh1w2cIjfQny5OG0vTBZkKZe",
            host="dpg-csq1s1dds78s73ddsfpg-a.oregon-postgres.render.com",
            port="5432"
        )
        return conn
    except Exception as e:
        print("An error occurred:", e)

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
    return f"this is the shadow with ID {shadow_id}"


def create_shadow():
    return "this creates a shadow"


def update_shadow(shadow_id):
    return f"this updates the shadow with ID {shadow_id}"


def delete_shadow(shadow_id):
    return f"this deletes the shadow with ID {shadow_id}"
