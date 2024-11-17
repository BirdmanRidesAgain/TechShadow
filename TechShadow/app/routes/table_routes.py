from flask import request
from ts_app import app
from queries.table_queries import create_connection, create_tables

@app.route("/connection")
def create_a_connection():
    return create_connection()

@app.route("/build_tables")
def create_the_tables():
    return create_tables()
