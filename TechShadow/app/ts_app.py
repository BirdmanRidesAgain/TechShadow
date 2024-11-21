import prefix
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from tsdb import create_connection


app = Flask(__name__, template_folder="../templates", static_folder="../static")


from routes import message_routes, shadow_routes, user_routes, template_routes, table_routes

prefix.use_PrefixMiddleware(app)
