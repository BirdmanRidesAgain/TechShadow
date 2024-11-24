def create_test_tables(conn):
    try:
        cur =  conn.cursor()
        # Table 1: Users
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                userID INTEGER PRIMARY KEY AUTOINCREMENT,
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
                opportunityID INTEGER PRIMARY KEY AUTOINCREMENT,
                position VARCHAR(100) NOT NULL,
                job_description TEXT,
                is_remote BOOLEAN DEFAULT FALSE,
                is_in_person BOOLEAN DEFAULT FALSE,
                status VARCHAR(20) NOT NULL,
                required_skills TEXT,
                location VARCHAR(100)
            );
        """)

        # Table 3: Messages
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Messages (
                messageID INTEGER PRIMARY KEY AUTOINCREMENT,
                userID INTEGER REFERENCES Users(userID),
                message_content TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                userID2 INTEGER REFERENCES Users(userID),
                responded_at TEXT,
                status VARCHAR(20) DEFAULT 'unread'
            );
        """)

        conn.commit()
        print("Tables created successfully")
    except Exception as e:
        print(f"An error occurred while creating test tables: {e}")
