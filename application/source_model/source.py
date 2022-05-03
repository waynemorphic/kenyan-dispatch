from nturl2path import url2pathname


class Source:
    '''
    news class to define the news source objects

    Args:
        id, name
    '''

    def __init__(self, id, name, url, language, description ):
        self.id = id
        self.name = name
        self.url = url
        self.language = language  
        self.description = description