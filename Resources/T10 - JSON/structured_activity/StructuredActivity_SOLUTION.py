import pandas as pd
import matplotlib.pyplot as plt
import os

file_dir = os.getcwd()


url = 'https://data.seattle.gov/resource/fire-911.json'

df = pd.read_json(url)

#print(df.head())
#print(df.columns)
df.dropna()

x = df['longitude']
y = df['latitude']
plt.scatter(x, y)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('Longitude against Latitude for Fire 911 calls in Seattle')
plt.savefig(file_dir + '/fire-911-locations.pdf')