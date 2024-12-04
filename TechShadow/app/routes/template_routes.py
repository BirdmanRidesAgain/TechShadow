'''Creates routes from static html files. 'template.html' used as a blueprint for all html routes.'''
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
    return render_template('signup.html')


@template_bp.route("/create-shadow", methods=["GET"])
def shadow():
    return render_template('create_shadow.html')
