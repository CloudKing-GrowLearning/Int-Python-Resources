from urllib.request import urlopen
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

file_dir = os.getcwd()
with urlopen("https://data.cityofnewyork.us/resource/734v-jeq5.json") as url:
   json_data = json.loads(url.read().decode())

data = pd.DataFrame.from_dict(json_data)
data.to_csv(file_dir + '/sat_data.csv', index=False)

data = pd.read_csv(file_dir + '/sat_data.csv')
data = data[data['sat_math_avg_score'] != 's']
data = data[data['sat_critical_reading_avg_score'] != 's']
data = data[data['sat_writing_avg_score'] != 's']

data['sat_math_avg_score'] = data['sat_math_avg_score'].astype('float')
data['sat_critical_reading_avg_score'] = data['sat_critical_reading_avg_score'].astype('float')
data['sat_writing_avg_score'] = data['sat_writing_avg_score'].astype('float')
data['num_of_sat_test_takers'] = data['num_of_sat_test_takers'].astype('int')

data.reset_index()
data.index = data['school_name']
data = data.sort_values('sat_math_avg_score', ascending=False)

reduced_data = data[['sat_math_avg_score', 'sat_critical_reading_avg_score', 'sat_writing_avg_score']]
print(reduced_data.head(10))
print(reduced_data.describe())

#Plots
reduced_data.plot.scatter(x='sat_math_avg_score', y='sat_writing_avg_score')
plt.tight_layout()
plt.title('Average SAT math versus writing scores by schools')
plt.ylabel('Average SAT writing score')
plt.xlabel('Average SAT math score')
plt.savefig(file_dir + '/sat_scores.png')