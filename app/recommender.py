import pickle

movies = pickle.load(open('./models/movies.pkl', 'rb'))
similarity = pickle.load(open('./models/similarity.pkl', 'rb'))

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return []
    idx = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recs = []
    for i in distances[1:6]:
        recs.append(movies.iloc[i[0]].title)
    return recs
