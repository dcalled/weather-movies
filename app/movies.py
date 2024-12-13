import urllib.parse
import os
import requests


def sendGetRequest(url):
    token = os.getenv("MOVIEDB_ACCESS_TOKEN")
    if token is None:
        return
    headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, timeout=5000)
    return response.json()


def searchMovies(query, page):
    url = f"https://api.themoviedb.org/3/search/movie?query={urllib.parse.quote(query)}&include_adult=false&language=en-US&page={page}"
    return sendGetRequest(url)["results"]


def getMovieByID(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    return sendGetRequest(url)
