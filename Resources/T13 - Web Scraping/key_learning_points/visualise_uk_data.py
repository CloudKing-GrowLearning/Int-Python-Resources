import pandas as pd
import matplotlib.pyplot as plt
import os

file_dir = os.getcwd()
file_name = file_dir + '/uk_data.csv'
data = pd.read_csv(file_name)


data.index = data['Name']
data["2016"] = data["2016"].str.replace(",","").astype('int')
del data['Name']
data.plot(kind='pie', y='2016', legend=False)
plt.title('Pie chart of 2016 population data')
plt.savefig('uk_data.png')

