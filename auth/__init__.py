from flask import Blueprint, render_template, abort # import blueprint, render template, and abort from flask
from jinja2 import TemplateNotFound # import TemplateNotFound error from jinja2

auth = Blueprint('auth', __name__, template_folder='templates') # initialize the bluetooth with the auth template in the `templates` template folder

@auth.route('/', defaults={'page': 'index'}) # make a default route if no page is specified
@auth.route('/<page>') # handle other routes
def show(page): # show page function
    try: # try
        return render_template(f'pages/{page}.html') # return the template with the page name
    except TemplateNotFound: # handle the TemplateNotFound exception
        abort(404) # send 404 to the client if template not found
