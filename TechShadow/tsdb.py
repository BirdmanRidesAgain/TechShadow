import psycopg2
import os
import sqlite3
from app.queries.tables_queries import create_test_tables


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Connect to PostgreSQL
def create_connection():
    try:
        if os.getenv("TESTING") == "1":
            conn = sqlite3.connect(":memory:")
            create_test_tables()
            return conn
        else:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            return conn
    except Exception as e:
        print("error connceting to db", e)
        return None
