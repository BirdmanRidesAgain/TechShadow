import psycopg2
from psycopg2 import sql
from tsdb import create_connection



# Function to create tables
def create_tables():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            # Table 1: Users
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    userID SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    is_mentor BOOLEAN DEFAULT FALSE,
                    is_shadower BOOLEAN DEFAULT FALSE,
                    field VARCHAR(200)
                );
            """)

            # Table 2: Opportunities
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Opportunities (
                    opportunityID SERIAL PRIMARY KEY,
                    position VARCHAR(100) NOT NULL,
                    job_description TEXT,
                    is_remote BOOLEAN DEFAULT FALSE,
                    is_in_person BOOLEAN DEFAULT FALSE,
                    status VARCHAR(20) CHECK (status IN ('open', 'pending', 'closed')) NOT NULL,
                    required_skills TEXT,
                    location VARCHAR(100)
                );
            """)

            # Table 3: Messages
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Messages (
                    messageID SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100),
                    message_content TEXT
                );
            """)

            conn.commit()
            print("Tables created successfully")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
    finally:
        if conn:
            conn.close()
        return "create tables"


def drop_tables():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                        Select tablename
                        FROM pg_tables
                        WHERE schemaname = 'public'
                        """)
            tables = cur.fetchall()
            for table in tables:
                cur.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")
            conn.commit()
    except Exception as e:
        print(f"error droppoing tables {e}")
    finally:
        if conn:
            conn.close()
        return "drop tables"
