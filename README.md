# Movie Recommendation System

## Overview

This project implements a Movie Recommendation System using machine learning techniques, specifically focusing on natural language processing (NLP) and cosine similarity to suggest similar movies based on user input.

## Dataset

The project utilizes two datasets:

- **tmdb_5000_movies.csv**: Contains information about various movies, including title, overview, genres, and keywords.
- **tmdb_5000_credits.csv**: Contains the cast and crew information for the movies.

## Key Features

- Data cleaning and preprocessing to ensure the quality of the dataset.
- Extraction and transformation of relevant features (genres, keywords, cast, crew) into a suitable format for analysis.
- Implementation of cosine similarity to measure the similarity between movies based on their descriptive tags.
- Functionality to recommend similar movies based on a selected movie title.

## Installation

To run this project, ensure you have the following libraries installed:

```bash
pip install pandas numpy nltk scikit-learn
```
