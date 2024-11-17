import prefix
from flask import Flask
from dotenv import load_dotenv

import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")


from routes import message_routes, shadow_routes, user_routes, template_routes

load_dotenv()
test_env = os.getenv("TEST")

prefix.use_PrefixMiddleware(app)
