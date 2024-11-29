import pytest
from tsdb import create_connection


def test_create_test_tables():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """
                        )
            tables = [row[0] for row in cur.fetchall()]
            assert "users" in tables
            assert "opportunities" in tables
            assert "messages" in tables
    finally:
        if conn:
            conn.close()

def test_seed_test_tables():
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            # test user table
            cur.execute("SELECT * from Users;")
            users = cur.fetchall()
            assert len(users) == 3
            for i in range(len(users)):
                assert users[i][1] == f'username_{i+1}'

            # test message table
            cur.execute("SELECT * from Messages;")
            messages = cur.fetchall()

            assert len(messages) == 3
            for i in range(len(messages)):
                assert messages[i][1] == 1

            # test shadow table
            cur.execute("SELECT * from Opportunities;")
            shadows = cur.fetchall()

            assert len(shadows) == 3
            for i in range(len(shadows)):
                assert shadows[i][1] == f'position_{i+1}'
    finally:
        if conn:
            conn.close()


# def test_drop_tables(test_client):
#     try:
#         test_client.get("/drop_tables")
#         conn = create_connection()
#         with conn.cursor() as cur:
#             cur.execute("""
#                         SELECT tablename
#                         FROM pg_tables
#                         WHERE chemaname= 'public';
#                         """)
#             tables = cur.fetchall()
#             assert len(tables) == 0
#     finally:

#         if conn:
#             conn.close()
