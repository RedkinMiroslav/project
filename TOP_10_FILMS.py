import pandas as pd

df = pd.read_csv("movies_dataset.csv")

films_of_year = df[df['Year'] == 2010]
top_rated_films = films_of_year.sort_values('Rating', ascending=False)
print(top_rated_films.head(10)[['Title', 'Year', 'Rating']])