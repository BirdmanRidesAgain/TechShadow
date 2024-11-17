from ts_app import app
from queries.tables_queries import create_tables


@app.route("/create_tables")
def create_tables_route():
    return create_tables()
