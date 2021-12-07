import pandas as pd

df1 = pd.read_csv('Spotify_dataset.csv')
df2= df1[df1['Artist'] == 'Chris Rea'].sort_values(by=['Song Name'])
print(df2)