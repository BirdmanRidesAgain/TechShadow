from flask import render_template
from ts_app import app


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/contact-us", methods=["GET"])
def contact_us():
    return render_template('contact_us.html')
