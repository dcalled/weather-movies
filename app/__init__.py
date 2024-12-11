from dotenv import load_dotenv
load_dotenv()
from .movies import searchMovies
from .weather import getTemperature
from flask import Flask

def create_app():
  app = Flask(__name__)

  from .routes import main
  app.register_blueprint(main)

  return app

query = "avatar fire"
page=1

movies = searchMovies(query, page)

print(movies)

date = "2024-12-09"
temps = getTemperature(date)
print(temps)