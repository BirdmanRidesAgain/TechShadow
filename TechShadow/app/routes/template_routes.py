from flask import render_template
from ts_app import app


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')
