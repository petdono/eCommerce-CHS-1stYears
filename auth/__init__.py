from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', defaults={'page': 'index'})
@auth.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)