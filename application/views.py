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
    
    # articles
    the_article = get_article()

    print(the_source)
    print(the_article)

    # render to template
    return render_template('index.html', heading = heading, the_source = the_source, the_article = the_article )
