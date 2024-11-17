from flask import jsonify
from ts_app import app
from queries.tables_queries import create_connection, create_tables

@app.route("/connection")
def create_a_connection():
    conn = create_connection()
    if conn:
        return "Connection successful!"
    else:
        return "Connection failed!", 500

@app.route("/build_tables")
def create_the_tables():
    conn = create_connection()
    if conn:
        # Return a success or error message from create_tables function
        try:
            create_tables(conn)
            conn.close()  # Ensure the connection is closed after use
            return jsonify({"status": "success", "message": "Tables created successfully"})
        except Exception as e:
            return jsonify({"status": "error", "message": f"Failed to create tables: {e}"}), 500
    else:
        return jsonify({"status": "error", "message": "Failed to connect to the database, tables not created"}), 500
