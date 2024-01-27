"""MichMoney API Init."""

import flask
import michmoney
import michmoney.api.admin
import michmoney.api.api_exceptions
import michmoney.api.auth
import michmoney.api.optimize
from michmoney.api.state import ApplicationState

# state = ApplicationState()  # Preload global resources on startup


@michmoney.app.route("/api/", methods=["GET", "POST"])
def api_default():
    """MichMoney API Usage Endpoint."""
    api_key = flask.request.headers.get("Authorization")
    if michmoney.api.admin.check_admin_priv(api_key):
        return flask.jsonify(
            {
                "/api/": "API Usage Info",
                "/api/account/": "View Account Details",
                "/api/db/status/": "Test Database Connection",
                "/api/db/dump/": "Dump Database",
                "/api/admin/add/": "Add Admin",
                "/api/admin/remove/": "Remove Admin",
                "/api/admin/user-info/": "Fetch User Info",
                "/api/admin/update-user/": "Update User Info",
                "/api/admin/delete-user/": "Delete User",
            }
        )
    return flask.jsonify(
        {
            "/api/": "API Usage Info",
            "/api/account/": "View Account Details",
        }
    )
