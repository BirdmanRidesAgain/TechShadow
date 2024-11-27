from flask import Blueprint, request, jsonify
from form_queries import save_message

form_routes = Blueprint('form_routes', __name__)

@form_bp.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    # Get form data from the request
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save the message using the function from form_queries.py
    result = save_message(name, email, message)

    return 