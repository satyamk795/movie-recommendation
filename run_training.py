from app.preprocess import load_data
from app.train_model import train

df = load_data()
train(df)
print("Model trained and saved!")
