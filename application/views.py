from flask import render_template
from application import app

# views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    heading = 'Kenyan Dispatch'
    return render_template('index.html', heading = heading)