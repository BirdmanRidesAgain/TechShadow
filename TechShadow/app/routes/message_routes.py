from ts_app import app


@app.route("/hello3")
def hello_world3():
    return "<p>Hello, World!</p>"
