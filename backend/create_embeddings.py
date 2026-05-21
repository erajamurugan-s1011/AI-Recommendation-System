import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import ast

movies = pd.read_csv("../data/tmdb_5000_movies.csv")

movies = movies[['title','overview','genres']]
movies = movies.dropna()

def extract_genres(obj):

    names=[]

    try:

        data=ast.literal_eval(obj)

        for item in data:
            names.append(item["name"])

        return " ".join(names)

    except:
        return ""

movies["genres"]=movies["genres"].apply(
    extract_genres
)

movies["combined"]=(
    movies["genres"]+" "+
    movies["overview"]
)

model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings=model.encode(
    movies["combined"].tolist(),
    show_progress_bar=True
)

np.save(
    "../models/movie_embeddings.npy",
    embeddings
)

movies.to_csv(
    "../models/processed_movies.csv",
    index=False
)

print("Saved successfully")