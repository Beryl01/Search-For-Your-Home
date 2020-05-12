from flask import render_template
from . import main

# your views go here i.e for home,about
@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')