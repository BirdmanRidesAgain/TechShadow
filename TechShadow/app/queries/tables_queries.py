import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="techshadowdb",
            user="techshadowdb_user",
            password="tftK4LBskh1w2cIjfQny5OG0vTBZkKZe",
            host="dpg-csq1s1dds78s73ddsfpg-a.oregon-postgres.render.com",
            port="5432" 
        )
        print("Connection successful!")
    except Exception as e:
        print("An error occurred:", e)


# Function to create tables
def create_tables(conn):
    try:
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
                    userID INTEGER REFERENCES Users(userID),
                    message_content TEXT,
                    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
                    userID2 INTEGER REFERENCES Users(userID),
                    responded_at TIMESTAMPTZ,
                    status VARCHAR(20) CHECK (status IN ('read', 'unread', 'draft')) DEFAULT 'unread'
                );
            """)

            conn.commit()
            print("Tables created successfully")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_tables(conn)
        conn.close()