from os import environ
from instance.config import API_KEY


class Config:
    '''
    parent class for general configuration
    '''
    NEWS_API_URL = 'https://newsapi.org/v2/everything?q=us&from=2022-05-03&to=2021-05-01&sortBy=popularity&language=en&apikey=a29b00af8b22470991b15e53f1eaa1b7'
    API_KEY = environ.get('API_KEY')
    SOURCE_URL = 'http://newsapi.org/v2/sources?category=general&language=en&apiKey=a29b00af8b22470991b15e53f1eaa1b7'
    # TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines/sources?country=us&category=general&language=en&apiKey={}'

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