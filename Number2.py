import pandas as pd

df1 = pd.read_csv('Spotify_dataset.csv')

df2 = df1[df1['Artist'] == 'Queen'].sort_values(by=['Song Name'])
print(df2['Artist'])
print(df2['Song Name'])
df3 = df1[df1['Artist'] == 'Ed Sheeran'].sort_values(by=['Song Name'])
print(df3['Artist'])
print(df3['Song Name'])
