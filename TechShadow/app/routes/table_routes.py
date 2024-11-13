from ts_app import app


@app.route("/build_tables")
def create_tables():
    return tables()
