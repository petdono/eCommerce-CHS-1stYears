from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    return render_template("index.html")