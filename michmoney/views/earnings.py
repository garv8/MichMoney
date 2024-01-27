"""Route and code for earnings-analyzer page.

GET /earnings-analyzer/"""

import flask
import michmoney
from michmoney.views.accounts import is_logged_in


@michmoney.app.route("/earnings-analyzer/", methods=["GET"])
def show_earnings():
    """Display /eearnings-analyzer route."""
    if is_logged_in() is False:
        return flask.redirect(flask.redirect("show_login"))
    context = {
        "user": {
            "is_authenticated": is_logged_in(),
        },
    }
    return flask.render_template("earnings.html", **context)
