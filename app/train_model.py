import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(i) for i in text.split()])

def train(df):
    df["tags"] = df["tags"].apply(stem)

    cv = CountVectorizer(max_features=3000, stop_words="english")
    vectors = cv.fit_transform(df["tags"]).toarray()

    similarity = cosine_similarity(vectors)

    pickle.dump(df, open('./models/movies.pkl', 'wb'))
    pickle.dump(similarity, open('./models/similarity.pkl', 'wb'))
