import pandas as pd

pd.set_option("display.max_rows", 200)
pd.set_option("display.max_columns", 100)


df1 = pd.read_csv('Spotify_dataset.csv')
df2 = df1[df1['Artist'] == 'Queen'].sort_values(by=['Song Name'])
print(df2)
print(df2)