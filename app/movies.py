import urllib.parse
import requests
import os
import urllib

def sendGetRequest(url):
  token = os.getenv("MOVIEDB_ACCESS_TOKEN")
  if token is None:
    return
  headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {token}"
  }
  response = requests.get(url, headers=headers)
  return response.json()

def searchMovies(query, page):
  url = f"https://api.themoviedb.org/3/search/movie?query={urllib.parse.quote(query)}&include_adult=false&language=en-US&page={page}"
  print(url)
  return sendGetRequest(url)['results']

def getMovieByID(id):
  url = f"https://api.themoviedb.org/3/movie/{id}"
  return sendGetRequest(url)