from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap # initializing bootstrap

# Application initialization
app = Flask(__name__)

# setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from application import views

