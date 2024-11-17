import prefix
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from tsdb import create_connection


app = Flask(__name__, template_folder="../templates", static_folder="../static")


from routes import message_routes, shadow_routes, user_routes, template_routes

@app.route("/testdb")
def test_db():
    conn = create_connection()
    if conn:
        with conn.cursor() as curr:
            curr.execute("SELECT 'db connect success'")
            message = curr.fetchone()
        conn.close()
        return message[0]
    else:
        return "failed to connect to db"

prefix.use_PrefixMiddleware(app)
