from os import environ
from instance.config import API_KEY


class Config:
    '''
    parent class for general configuration
    '''
    NEWS_API_URL = 'https://newsapi.org/v2/everything?q={}apikey={}'
    API_KEY = environ.get('API_KEY')

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