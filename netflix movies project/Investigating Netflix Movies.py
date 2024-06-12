# Investigating Netflix Movies

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter data for movies from the 1990s
nineties_movies = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000) & (netflix_df['type'] == 'Movie')]
# Find the most frequent duration
most_frequent_duration = nineties_movies['duration'].mode()[0]
print("The most frequent movie duration in the 1990s:", most_frequent_duration)

# Filter for short action movies from the 1990s
short_action_movies_90s = nineties_movies[(nineties_movies['duration'] < 90) & (nineties_movies['genre'].str.contains('Action'))]

# Count of short action movies
short_movie_count = len(short_action_movies_90s)
print("Number of short action movies released in the 1990s:", short_movie_count)