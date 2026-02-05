from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

// initialize main blueprint
main = Blueprint('main', __name__, template_folder='templates')

// main route
@main.route('/', defaults={'page': 'index'})
@main.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404) // 404, handle later with 404 page
