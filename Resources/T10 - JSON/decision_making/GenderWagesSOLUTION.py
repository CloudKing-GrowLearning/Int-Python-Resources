import json, urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with urllib.request.urlopen("https://data.seattle.gov/resource/5m8y-83zb.json") as url:
  json_data = json.loads(url.read().decode())
  data = pd.DataFrame.from_dict(json_data)

  num_group = 4

  avg_male = data['male_avg_hrly_rate'][:num_group]
  avg_female = data['female_avg_hrly_rate'][:num_group]
  jobtitle_list = data['jobtitle']

  for i in range(0, len(avg_male)):
      avg_male[i] = float(avg_male[i])
      avg_female[i] = float(avg_female[i])

  #Create Plot
  fig, ax = plt.subplots()
  #index = np.arange(num_group)
  index = pd.Series(range(num_group))
  bar_width = 0.35
  opacity = 0.8

  rects1 = plt.bar(index, avg_male, bar_width,
                   alpha=opacity,
                   color='r',
                   label='Male')

  rect2 = plt.bar(index + bar_width, avg_female, bar_width,
                  alpha=opacity,
                  color='g',
                  label='Female')

  plt.xlabel('Department')
  plt.ylabel('Average Hourly Rate')
  plt.title('Comparison of Wages between Genders Across City Departments')
  plt.xticks(index + (bar_width / 2), jobtitle_list[:num_group], rotation='vertical')
  plt.legend()

  plt.tight_layout()
  plt.show()