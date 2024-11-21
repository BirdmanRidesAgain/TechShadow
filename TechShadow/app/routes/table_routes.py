from flask import jsonify, Blueprint
from queries.tables_queries import create_tables

table_bp = Blueprint("tables", __name__)

@table_bp.route("/create_tables")
def create_tables_route():
    return create_tables()
