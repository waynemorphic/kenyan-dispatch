class News:
    '''
    news class to define the news objects

    Args:
        Author, Title, Description, Url
    '''

    def __init__(self, author, title, description, url, image ):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = 'https://s.yimg.com/os/creatr-uploaded-images/2020-07/c9ee07d0-c117-11ea-b67f-851aefcf30f2' 