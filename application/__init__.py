
from flask import Flask
from .config import DevConfig

# Application initialization
app = Flask(__name__)

# setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from application import views

