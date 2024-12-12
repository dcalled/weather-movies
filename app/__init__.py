from dotenv import load_dotenv
load_dotenv()
from .movies import searchMovies, getMovieByID
from .weather import getTemperature
from flask import Flask

def create_app():
  app = Flask(__name__)

  from .routes import main
  app.register_blueprint(main)

  return app

query = "avatar"
page=1

movies = searchMovies(query, page)
movie = movies[0]

#print(movie)

fullMovie = getMovieByID(movie['id'])
print(fullMovie)

date = fullMovie['release_date']
temps = getTemperature(date)
print(temps)

data = {
  'title': fullMovie['title'],
  'genres': list(map(lambda x: x['name'], fullMovie['genres'])),
  'maxTemp': temps['daily']['temperature_2m_max'][0],
  'minTemp': temps['daily']['temperature_2m_min'][0],
}

print(data)

