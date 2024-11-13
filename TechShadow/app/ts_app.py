import prefix

from flask import Flask

app = Flask(__name__, template_folder="../templates", static_folder="../static")

prefix.use_PrefixMiddleware(app)

from routes import message_routes, shadow_routes, user_routes, template_routes
