from ts_app import app
from queries.shadow_queries import get_shadows


@app.route("/shadows")
def get_all_shadows():
    return get_shadows()
