import prefix
import os
import sys
from flask import Flask
from dotenv import load_dotenv

load_dotenv()



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__, template_folder="../templates", static_folder="../static")

app.config["DB_USER"] = os.getenv("DB_USER")
app.config["DB_PASSWORD"] = os.getenv("DB_PASSWORD")
app.config["DB_HOST"] = os.getenv("DB_HOST")
app.config["DB_PORT"] = os.getenv("DB_PORT")
app.config["DB_NAME"] = os.getenv("DB_NAME")

from routes.message_routes import message_bp
from routes.shadow_routes import shadow_bp
from routes.user_routes import user_bp
from routes.template_routes import template_bp
from routes.table_routes import table_bp


@app.route("/test")
def test_route():
    return "TEST IS RUNNING"


app.register_blueprint(message_bp)
app.register_blueprint(shadow_bp)
app.register_blueprint(user_bp)
app.register_blueprint(template_bp)
app.register_blueprint(table_bp)

if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("PORT", os.getenv("FLASK_RUN_PORT", 5000)))
    app.run(host=host, port=port, use_reloader=False)
