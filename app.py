import pickle
import streamlit as st
import requests
import pandas as pd  # Importing pandas with an alias is standard practice
import gdown
import os
import gzip

# Google Drive file ID for similarity.pkl
file_id = "1IySoaWD5cDSdLx--lfdQLJ6kpLiuouqD"
url = f"https://drive.google.com/uc?id={file_id}"
output = "similarity.pkl"

# Download the file if it does not exist
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)


# Function to fetch movie posters from TMDb API
def fetch_poster(movie_id):
    api_key = "2a502fe5ec57b17eaf7aed2ebeae91fa"  # Replace with your own API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    # Return a placeholder image URL if no poster is found
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"


# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    recommended_movies_name = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies_name, recommended_movies_poster


# Streamlit UI
st.header("Movies Recommendation System Using Machine Learning")

# Load movie data
movies = pickle.load(open("movies.pkl", "rb"))

# Load similarity matrix with error handling
try:
    similarity = pickle.load(open("similarity.pkl", "rb"))
except FileNotFoundError:
    st.error(
        "Error: similarity.pkl not found! Ensure the file is correctly downloaded."
    )
    st.stop()

# Streamlit dropdown for movie selection
movie_list = movies["title"].values
selected_movie = st.selectbox(
    "Type or select a movie to get recommendations:", movie_list
)

# Show recommendations when button is clicked
if st.button("Show Recommendations"):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(recommended_movies_name[i])
            st.image(recommended_movies_poster[i])
