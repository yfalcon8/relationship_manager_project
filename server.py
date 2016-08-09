"""My web app's online structure."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, redirect, session
from flask_debeugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User

app = Flask(__name__)

# Required to use Flask sessions and the debug DebugToolbarExtension
app.secret_key = "ILoveStephenColbert"

# Raises an error when an undefined variable is used in Jinja2.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")
