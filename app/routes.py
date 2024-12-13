from flask import Blueprint, request, jsonify
from .movies import searchMovies, getMovieByID
from .weather import getTemperature

api = Blueprint("api", __name__)


@api.route("/movie-info", methods=["GET"])
def movie_info():
    page = 1
    query = request.args.get("query")

    if not query:
        return jsonify({"error": "Query string is required"}), 400

    # Fetch movies
    movies = searchMovies(query, page)
    if not movies:
        return jsonify({"error": "No movies found"}), 404

    movie = movies[0]

    # Fetch full movie details
    full_movie = getMovieByID(movie["id"])
    if not full_movie or "release_date" not in full_movie:
        return jsonify({"error": "No detailed movie information found"}), 404

    # Fetch weather data
    date = full_movie["release_date"]
    temps = getTemperature(date)
    if not temps or "daily" not in temps:
        return jsonify({"error": "No weather data available"}), 404

    # Prepare response data
    data = {
        "title": full_movie["title"],
        "genres": [genre["name"] for genre in full_movie.get("genres", [])],
        "maxTemp": temps["daily"]["temperature_2m_max"][0],
        "minTemp": temps["daily"]["temperature_2m_min"][0],
    }

    return jsonify(data)
