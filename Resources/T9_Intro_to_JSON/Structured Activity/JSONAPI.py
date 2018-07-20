import json, urllib.request
import pandas as pd
import matplotlib.pyplot as plt


with urllib.request.urlopen("https://data.seattle.gov/resource/fire-911.json") as url:
    json_data = json.load(url)

    data = pd.DataFrame.from_dict(json_data)

    x = data['longitude']
	y = data['latitude']

	plt.scatter(x, y)#using matPlotLib
	plt.title('Scatterplot of Fire 911 data by Lat and Long')
	plt.xlabel('Longitude')
	plt.ylabel('Latitude')

	plt.show()