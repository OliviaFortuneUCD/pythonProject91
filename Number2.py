import pandas as pd

df1 = pd.read_csv('Spotify_dataset.csv')

df2 = df1[df1['Artist'] == 'Ariana Grande'].sort_values(by=['Song Name']).head(5)
print(df2)
