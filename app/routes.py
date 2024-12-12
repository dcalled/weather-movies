from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, Flask!"

@main.route('/search/movie')
def home():
    return "Hello, Flask!"