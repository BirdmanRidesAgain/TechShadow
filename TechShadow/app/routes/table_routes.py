'''Implements database access/posting methods for our table queries.'''
from flask import jsonify, Blueprint
from queries.tables_queries import create_tables, drop_tables

table_bp = Blueprint("tables", __name__)


@table_bp.route("/create_tables")
def create_tables_route():
    return create_tables()


# @table_bp.route("/drop_tables")
# def drop_tables_route():
#     return drop_tables()
