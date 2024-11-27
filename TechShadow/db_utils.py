def create_test_tables(conn):
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
                    userID INTEGER REFERENCES Users(userID) ON DELETE CASCADE,
                    message_content TEXT,
                    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
                    userID2 INTEGER REFERENCES Users(userID) ON DELETE CASCADE,
                    responded_at TIMESTAMPTZ,
                    status VARCHAR(20) CHECK (status IN ('read', 'unread', 'draft')) DEFAULT 'unread'
                );
            """)

            conn.commit()
    except Exception as e:
        print(f"An error occurred while creating test tables: {e}")

def truncate_test_tables(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE Users RESTART IDENTITY CASCADE;")
            cur.execute("TRUNCATE TABLE Opportunities RESTART IDENTITY CASCADE;")
            cur.execute("TRUNCATE TABLE Messages RESTART IDENTITY CASCADE;")
            conn.commit()
    except Exception as e:
        print(f"An error occurred while truncating test tables: {e}")


def seed_test_tables(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT into Users (username, password, first_name, last_name, is_mentor, is_shadower, field)
                VALUES ('username_1', 'password_1', 'first_name_1', 'last_name_1', True, False, 'field_1'),
                    ('username_2', 'password_2', 'first_name_2', 'last_name_2', True, False, 'field_2'),
                    ('username_3', 'password_3', 'first_name_3', 'last_name_3', True, False, 'field_3');
            """)

            cur.execute("""
                INSERT into Opportunities (position, job_description, is_remote, is_in_person, status, required_skills, location)
                VALUES ('position_1', 'job_description_1', True, False, 'open', 'required_skills_1', 'location_1'),
                    ('position_2', 'job_description_2', True, False, 'open', 'required_skills_2', 'location_2'),
                    ('position_3', 'job_description_3', True, False, 'open', 'required_skills_3', 'location_3');
            """)

            cur.execute("""
                INSERT into Messages (userID, message_content, userID2, status)
                VALUES (1, 'message_content_1', 2, 'unread'),
                    (1, 'message_content_2', 2, 'unread'),
                    (1, 'message_content_3', 2, 'unread');
            """)

            conn.commit()
    except Exception as e:
        print(f"An error occurred while seeding test tables: {e}")
