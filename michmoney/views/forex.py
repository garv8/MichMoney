"""Route and code for forex page.

GET /forex/"""

import flask
import michmoney
from michmoney.views.accounts import is_logged_in


@michmoney.app.route("/forex/", methods=["GET"])
def show_forex():
    """Display /forex route."""
    if is_logged_in() is False:
        return flask.redirect(flask.redirect("show_login"))
    context = {
        "user": {
            "is_authenticated": is_logged_in(),
        },
    }
    return flask.render_template("forex.html", **context)
