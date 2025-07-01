import pandas as pd
import ast

def load_data():
    movies = pd.read_csv('./data/tmdb_5000_movies.csv')
    credits = pd.read_csv('./data/tmdb_5000_credits.csv')

    movies = movies.merge(credits, on='title')

    movies = movies[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]
    movies.dropna(inplace=True)

    def parse(name_field):
        return [i["name"].replace(" ", "") for i in ast.literal_eval(name_field)]

    def get_director(crew_str):
        for i in ast.literal_eval(crew_str):
            if i["job"] == "Director":
                return [i["name"].replace(" ", "")]
        return []

    movies["genres"] = movies["genres"].apply(parse)
    movies["keywords"] = movies["keywords"].apply(parse)
    movies["cast"] = movies["cast"].apply(lambda x: parse(x)[:5])
    movies["crew"] = movies["crew"].apply(get_director)
    movies["overview"] = movies["overview"].apply(lambda x: x.split())

    for col in ["cast", "crew", "genres", "keywords", "overview"]:
        movies[col] = movies[col].apply(lambda x: [i.replace(" ", "") for i in x])

    movies["tags"] = movies["overview"] + movies["genres"] + movies["keywords"] + movies["cast"] + movies["crew"]
    df = movies[["movie_id", "title", "tags"]]
    df["tags"] = df["tags"].apply(lambda x: " ".join(x))

    return df
