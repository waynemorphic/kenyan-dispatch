class Article:
    '''
    class to define the articles object

    Args:
    author, title, description, url, urlToImage
    '''

    def __init__(self, author, title, description, url, urlToImage, publishedAt):
        '''
        object initialization
        '''
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

