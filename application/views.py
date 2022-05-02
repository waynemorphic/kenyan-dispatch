from flask import render_template
from application import app
from .request import get_article, get_news_source

# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # retrieving news source from the API with name and id
    heading = 'Kenyan Dispatch'

    # sources
    source_id = get_news_source('id')
    source_name = get_news_source('name')
    

    # articles
    article_author = get_article('author')
    article_title = get_article('title')
    article_description = get_article('description')
    article_url = get_article('url')
    article_urlToImage = get_article('urlToImage')
  
    return render_template('index.html', heading = heading, id = source_id, name = source_name, author = article_author, title = article_title, description = article_description, url = article_url, urlToImage = article_urlToImage)