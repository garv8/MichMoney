"""Route and code for login page.

GET /login/
"""

import michmoney
from flask import render_template

@michmoney.app.route('/login/', methods=['GET'])
def show_login():
    """Display /login route."""
    context = {}
    return render_template("login.html", **context)
