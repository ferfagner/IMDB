from flask import Flask

imdb = Flask(__name__, template_folder='../templates', static_folder='../static')

from control import imdb_control

imdb.run()
