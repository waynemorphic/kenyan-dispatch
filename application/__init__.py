from flask import Flask
from config import DevConfig

# Application initialization
app = Flask(__name__)

# setting up configurations
app.config.from_object(DevConfig)

from application import views

