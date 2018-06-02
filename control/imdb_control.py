from flask import render_template
from control import imdb

@imdb.route('/')
def home():
 return render_template('index.html')
@imdb.route('/about')
def about():
 return render_template('about.html')



