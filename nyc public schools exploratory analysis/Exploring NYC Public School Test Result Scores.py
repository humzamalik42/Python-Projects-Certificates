# Exploring NYC Public School Test Result Scores

import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Assuming 'total_SAT' is the sum of math, reading, and writing scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# Filter schools with best math results
best_math_schools = schools[schools['average_math'] >= 0.8 * 800].copy()
best_math_schools = best_math_schools.sort_values('average_math', ascending=False)[['school_name', 'average_math']]

# Display the results
print(best_math_schools)

# Sort schools by total SAT scores in descending order and select top 10
top_10_schools = schools.sort_values('total_SAT', ascending=False).head(10)
top_10_schools = top_10_schools[['school_name', 'total_SAT']]

# Display the results
print(top_10_schools)

# Calculate statistics by borough
borough_stats = schools.groupby('borough').agg(
    num_schools=pd.NamedAgg(column="school_name", aggfunc="count"),
    average_SAT=pd.NamedAgg(column="total_SAT", aggfunc=lambda x: round(x.mean(), 2)),  # Round mean to 2 decimal places
    std_SAT=pd.NamedAgg(column="total_SAT", aggfunc=lambda x: round(x.std(), 2))  # Round std dev to 2 decimal places
)

# Find the borough with the largest standard deviation
largest_std_dev = borough_stats[borough_stats['std_SAT'] == borough_stats['std_SAT'].max()].reset_index()

# Optionally, round all numeric values in the resulting DataFrame
largest_std_dev[['num_schools', 'average_SAT', 'std_SAT']] = largest_std_dev[['num_schools', 'average_SAT', 'std_SAT']].apply(lambda x: round(x, 2))

# Display the result
print(largest_std_dev)