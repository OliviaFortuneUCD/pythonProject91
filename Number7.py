import pandas as pd



df1 = pd.read_csv('Spotify_dataset.csv')


print(df1[df1['Song Name'].str.contains("Christmas")])
