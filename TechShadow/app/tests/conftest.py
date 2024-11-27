import pytest
import os
import sys
from ts_app import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db_utils import create_test_tables, truncate_test_tables, seed_test_tables
from tsdb import create_connection


os.environ["DB_USER"] = os.getenv("TEST_DB_USER")
os.environ["DB_PASSWORD"] = os.getenv("TEST_DB_PASSWORD")
os.environ["DB_HOST"] = os.getenv("TEST_DB_HOST")
os.environ["DB_PORT"] = os.getenv("TEST_DB_PORT")
os.environ["DB_NAME"] = os.getenv("TEST_DB_NAME")

@pytest.fixture
def test_client():
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture(scope="session", autouse=True)
def test_db_create():
    conn = create_connection()
    if conn:
        create_test_tables(conn)
        conn.close()
    else:
        raise RuntimeError("Failed to connect to test database")

@pytest.fixture(autouse=True)
def test_db_setup():
    conn = create_connection()
    if conn:
        truncate_test_tables(conn)
        seed_test_tables(conn)
        conn.close()
    else:
        raise RuntimeError("Failed to reset test dbs")
