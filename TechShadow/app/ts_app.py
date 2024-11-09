import prefix

from flask import Flask

app = Flask(__name__)

prefix.use_PrefixMiddleware(app)

from routes import message_routes, shadow_routes, user_routes
