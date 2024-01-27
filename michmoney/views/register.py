"""Route and code for login page.

GET /login/
"""

import michmoney
from flask import render_template


@michmoney.app.route('/register/', methods=['GET'])
def show_register():
    """Display /register route."""
    context = {}
    return render_template("register.html", **context)
