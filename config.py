class Config:
    '''
    parent class for general configuration
    '''
    pass

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