import pickle
import streamlit as st
import requests
import pandas as pd  # Importing pandas with an alias is standard practice
import gzip


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2a502fe5ec57b17eaf7aed2ebeae91fa"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    # Return a placeholder image URL if no poster is found
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"


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


# Load compressed similarity.pkl.gz
@st.cache_resource
def load_similarity():
    with gzip.open("similarity.pkl.gz", "rb") as f:
        return pickle.load(f)


st.header("Movies Recommendation System Using Machine Learning")
movies = pickle.load(open("movies.pkl", "rb"))
similarity = load_similarity()

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie to get recommendations:", movie_list
)

if st.button("Show Recommendations"):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(recommended_movies_name[i])
            st.image(recommended_movies_poster[i])
