"""Route and code for landing (index) page.

GET /
"""

from flask import render_template
import michmoney
from michmoney.views.accounts import is_logged_in


@michmoney.app.route("/", methods=["GET"])
def show_landing():
    """Display / route."""
    context = {
        "user": {
            "is_authenticated": is_logged_in(),
        },
    }
    return render_template("index.html", **context)
