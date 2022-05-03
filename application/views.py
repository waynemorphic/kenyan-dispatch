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
    the_source = get_news_source()
    the_article = get_article()

    print(the_source)
    print(the_article)
    # source_n = get_news_source()
    # # #source_url = get_news_source('url')
    # article_w = get_article()

    # # articles
    # article_author = get_article('author')
    # article_title = get_article('title')
    # article_description = get_article('description')
    # article_url = get_article('url')
    # article_urlToImage = get_article('urlToImage')
    # print(article_description)
   
    # return render_template('index.html', heading = heading, name = source_name, language = source_language, author = article_author, title = article_title, description = article_description, url = article_url, urlToImage = article_urlToImage)

    return render_template('index.html', heading = heading, the_source = the_source, the_article = the_article )
