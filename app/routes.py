from flask import render_template, request
from app import app
from app.recommender import movies, recommend

@app.route("/", methods=["GET", "POST"])
def index():
    movie_list = sorted(
        movies["title"].values,
        key=lambda s: s.lower().strip("#") if isinstance(s, str) else ""
    )
    recommendations = None
    selected_movie = None

    if request.method == "POST":
        selected_movie = request.form.get("movie_search")
        recommendations = recommend(selected_movie)

    return render_template(
        "index.html",
        movie_list=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie
    )
