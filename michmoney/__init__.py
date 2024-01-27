"""Initializer for michmoney module."""
from flask import Flask

app = Flask(__name__)

app.config.from_object("michmoney.config")

# app.config.from_envvar("MICHMONEY_SETTINGS", silent=True)

import michmoney.api
import michmoney.model
import michmoney.views
import michmoney.templates
