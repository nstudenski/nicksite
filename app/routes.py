from flask import render_template
from app import app

@app.route('/')

@app.route('/index')

def index():
    user = {'username': 'Nick'}
    posts = [
	    {
	    	'author': {'username':'Nick'},
	    	'body': 'Went to work today'
	    },
	    {
	    	'author': {'username':'Nick'},
	    	'body': 'I worked again today'
	    }
    ]
    return render_template('index.html', user=user, posts = posts)