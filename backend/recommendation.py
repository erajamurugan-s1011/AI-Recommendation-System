import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load dataset
movies = pd.read_csv("../data/tmdb_5000_movies.csv")

# Keep useful columns and remove missing rows
movies = movies[['title','overview','genres']]
movies = movies.dropna()


# Function to extract genre names
def extract_genres(obj):

    genre_list = []

    try:
        genres = ast.literal_eval(obj)

        for item in genres:
            genre_list.append(item['name'])

        return " ".join(genre_list)

    except:
        return ""


# Convert genre JSON text to plain text
movies['genres'] = movies['genres'].apply(
    extract_genres
)

# Combine text for embeddings
movies["combined"] = (
    movies["genres"] + " " +
    movies["overview"]
)

print("Creating embeddings... First run may take some time")

# Load model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Create embeddings
embeddings = model.encode(
    movies["combined"].tolist(),
    show_progress_bar=True
)


def recommend(user_input):

    user_embedding = model.encode(
        [user_input]
    )

    similarity = cosine_similarity(
        user_embedding,
        embeddings
    )

    top_indices = similarity[0].argsort()[-5:][::-1]

    recommendations = movies.iloc[top_indices]

    return recommendations["title"].tolist()