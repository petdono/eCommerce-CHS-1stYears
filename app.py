from flask import Flask
from main import main
from auth import auth

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')