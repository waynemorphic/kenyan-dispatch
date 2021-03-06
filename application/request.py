from application.articles_model.articles import Article
from application import app
import urllib.request,json
from application.source_model.source import Source

# retrieving the api key
api_key = app.config['API_KEY']

# retrieving news API base url
base_url = app.config['NEWS_API_URL']

# sources url
source_url = app.config['SOURCE_URL']

# API call
# get news article source
def get_news_source():
    '''
    function gets the json response to our url request for the news articles

    has source as an argument
    '''

    get_source_url = source_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_source = None

        if get_news_response['sources']:
            news_source_list = get_news_response['sources']
            news_source = process_source(news_source_list)
    print()
    return news_source

    # processing source

def process_source(source_list):
        '''
        function processes the news sources and transfroms them to a list of objects
        
        Args:
        source_list is a list of dictionaries that contains id and name of the news source
        
        Returns:
        news_source, which is a list of news sources objects
        '''

        news_source = []
        # list of dictionaries

        # looping through the list of dictionararies and passing in the keys to access values
        for source_item in source_list:
            id = source_item.get('id')
            name = source_item.get('name')
            url = source_item.get('url')
            language = source_item.get('language')
            description = source_item.get('description')

            # checking if name of source of news is available. If available, the source object is created
            if name:
                source_object = Source(id, name, url, language, description)
                news_source.append(source_object)

        return news_source
            

def get_article():
    '''
    function gets json response
    '''
    # get_article_url = base_url.format(api_key)
    get_article_url = 'https://newsapi.org/v2/everything?q=kenya&from=2022-05-01&sortBy=popularity&language=en&apikey=a29b00af8b22470991b15e53f1eaa1b7'   


    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        news_article = None

        if get_article_response['articles']:
            news_article_list = get_article_response['articles']
            news_article = process_article(news_article_list)

    return news_article

def process_article(article_list):
    '''
    function processes results and transforms them into list objects    
    '''
    news_article = []

    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if title:
            article_object = Article(author, title, description, url, image, publishedAt)
            news_article.append(article_object)

    return news_article

