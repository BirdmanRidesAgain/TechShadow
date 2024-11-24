from flask import render_template, Blueprint

template_bp = Blueprint("templates", __name__)


@template_bp.route("/", methods=["GET"])
def home():
    return render_template('home.html')


@template_bp.route("/contact-us", methods=["GET"])
def contact_us():
    return render_template('contact_us.html')


@template_bp.route("/signup", methods=["GET"])
def signup():
    return render_template('sign_up.html')
