from flask import render_template
from control import imdb

@imdb.route('/')
def home():
 return render_template('imdb_pag/index.html')



