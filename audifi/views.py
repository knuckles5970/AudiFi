"""
define routes and the contents returned
"""
from flask import Blueprint
from flask.templating import render_template
#from models import Park, Report

views = Blueprint('audifi', "views")


@views.route("/")
def root_path():
    return render_template("index.html")
