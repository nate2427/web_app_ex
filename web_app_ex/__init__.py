"""
Web App Example package initializer.
Nate Baker <natebaker2427@gmail.com>
"""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (web_app_ex/config.py)
app.config.from_object('web_app_ex.config')


import web_app_ex.views
