# Movie Recommendation System

## Overview

This project is a **Content-Based Movie Recommendation System** that suggests movies based on their similarity to a given movie. It analyzes movie descriptions, genres, and cast information to find and recommend the most relevant movies.

## Features

- **Content-Based Filtering** using **Cosine Similarity** to recommend movies.
- **Dynamic Poster Fetching** from **TMDb API** for better user experience.
- **Streamlit Web Interface** for an interactive and easy-to-use application.
- **Optimized Deployment** on **Render** for cloud accessibility.

## Technologies Used

- **Python 3.8** for backend logic.
- **Pandas & NumPy** for data processing.
- **Scikit-learn** for similarity calculations.
- **Streamlit** for web app development.
- **Gunicorn** for deploying the application.

## Dataset

The project uses **TMDb 5000 Movies Dataset**, which consists of:

- `tmdb_5000_movies.csv` - Contains movie titles, genres, and descriptions.
- `tmdb_5000_credits.csv` - Contains cast and crew details.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Create a Virtual Environment

```bash
conda create --name mrs_venv python=3.8
conda activate mrs_venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project Locally

To start the **Streamlit** application, run:

```bash
streamlit run app.py
```

## Deployment on Render

### 1. Push the project to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Deploy on Render

1. **Go to Render** and create a new web service.
2. **Connect your GitHub repository**.
3. **Set the build command**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set the start command**:
   ```bash
   streamlit run app.py --server.port 10000
   ```
5. Click **Deploy** and wait for the app to go live.

## Handling Large Files (similarity.pkl)

### Compress the File

Since `similarity.pkl` is too large for GitHub (100MB limit), compress it before uploading:

```python
import pickle
import gzip

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

with gzip.open("similarity.pkl.gz", "wb") as f:
    pickle.dump(similarity, f)
```

### Modify `app.py` to Load the Compressed File

```python
import pickle
import gzip
import streamlit as st

@st.cache_resource
def load_similarity():
    with gzip.open("similarity.pkl.gz", "rb") as f:
        return pickle.load(f)

similarity = load_similarity()
```

## Project Structure

```
movie-recommendation-system/
│── app.py                # Streamlit app
│── movies.pkl            # Processed movies dataset
│── similarity.pkl.gz     # Compressed similarity matrix
│── requirements.txt      # Dependencies
│── Procfile              # Deployment config (for Render)
│── README.md             # Project documentation
```

## Important Interview Questions

1. **What is a Content-Based Recommendation System?**
   - A system that recommends movies based on the similarity of their features (e.g., genres, actors, plot keywords).
2. **How does Cosine Similarity work in recommendations?**
   - It measures the similarity between two vectors (movies) based on their angle in multi-dimensional space.
3. **What are the limitations of Content-Based Filtering?**
   - Cannot recommend new movies without enough feature data (**cold start problem**).
   - Only finds similar items, not diverse recommendations.
4. **How does Streamlit work for web applications?**
   - Streamlit is a Python library that allows easy and quick development of web-based data applications.
5. **Why do we use `gzip` to compress files in deployment?**
   - It reduces file size, making it easier to upload large models or data files.
6. **How do you optimize a large `.pkl` file for cloud deployment?**
   - Compress using `gzip` or split the dataset into smaller chunks.
   - Store in cloud storage (e.g., Google Drive, AWS S3) and fetch dynamically.
7. **What are alternative recommendation approaches besides Content-Based Filtering?**
   - **Collaborative Filtering** (based on user behavior, e.g., Netflix).
   - **Hybrid Models** (combining Content-Based & Collaborative Filtering).

## License

This project is for educational purposes only.

---

**Created by Mohammad Anas**
