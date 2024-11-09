from ts_app import app


@app.route("/hello2")
def hello_world2():
    return "<p>Hello, World!</p>"
