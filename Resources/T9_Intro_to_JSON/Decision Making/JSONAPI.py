import json, urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with urllib.request.urlopen("https://data.seattle.gov/resource/5m8y-83zb.json") as url:
    json_data = json.loads(url.read().decode())

    data = pd.DataFrame.from_dict(json_data)
    #data.to_csv('out.csv')

    avg_male = data['male_avg_hrly_rate'][:4]
    avg_female = data['female_avg_hrly_rate'][:4]
    jobtitle_list = data['jobtitle']
    #print(avg_female)

    #Create Plot
    fig, ax = plt.subplots()
    num_group = 4
    index = np.arange(num_group)
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

    plt.xlabel('Gender')
    plt.ylabel('Average Hourly Rate')
    plt.title('Comparison of Gender Wages between Genders')
    plt.xticks(index + bar_width, (jobtitle_list[0], jobtitle_list[1], jobtitle_list[2], jobtitle_list[3]))
    plt.legend()

    plt.tight_layout()
    plt.show()

    #rect1 = ax.bar(ind, avg_male, width, color='r')

    #plt.show()