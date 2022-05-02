from os import environ
from instance.config import API_KEY


class Config:
    '''
    parent class for general configuration
    '''
    NEWS_API_URL = 'https://newsapi.org/v2/everything?q={}&apikey={}'
    API_KEY = environ.get('API_KEY')
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apikey=319a22ef8acc48d2a8bc83653dab0ed4'

class ProdConfig(Config):
    '''
    child class for production configuration 

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    child class for development configuration 

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True