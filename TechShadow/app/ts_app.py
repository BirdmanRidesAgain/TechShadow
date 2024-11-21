import prefix
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from tsdb import create_connection


app = Flask(__name__, template_folder="../templates", static_folder="../static")


from routes import message_routes, shadow_routes, user_routes, template_routes, table_routes


if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port)
