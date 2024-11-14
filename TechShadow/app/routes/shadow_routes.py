from flask import request, render_template
from ts_app import app
from queries.shadow_queries import get_shadows, get_shadow, create_shadow, update_shadow, delete_shadow

@app.route('/shadows')  
def shadow():
    shadows = get_shadows() 
    return render_template('shadows.html', shadows=shadows)


@app.route("/shadow", methods=["POST"])
def post_shadow():
    return create_shadow()


@app.route("/shadow/<int:shadow_id>", methods=["GET", "PUT", "DELETE"])
def get_one_shadow(shadow_id):
    if request.method == "GET":
        return render_template('base_template.html')
    elif request.method == "PUT":
        return update_shadow(shadow_id)
    elif request.method == "DELETE":
        return delete_shadow(shadow_id)
