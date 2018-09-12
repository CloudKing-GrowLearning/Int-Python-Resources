import pandas as pd
import matplotlib.pyplot as plt
import os

file_dir = os.getcwd()
file_name = file_dir + '/met_areas.csv'
data_df = pd.read_csv(file_name)

values = ['New York - Newark - Jersey City', 'Chicago - Naperville - Elgin', 'Los Angeles - Long Beach - Anaheim', 'San Francisco - Oakland - Hayward']

red_data = data_df[data_df['area_name'].isin(values)]

red_data.plot.bar(x='area_name')
plt.xticks([0,1,2,3],['Chicago', 'Los Angeles', 'New York','San Francisco'])
plt.tight_layout()
plt.title('Population Values Over Time')
plt.ylabel('Population (Millions)')
plt.xlabel('Area Name')
file_name = file_dir + '/absolute_change.pdf'
plt.savefig(file_name)

data_df['1990-2000'] = data_df['2000']/data_df['1990']
data_df['2000-2010'] = data_df['2010']/data_df['2000']
data_df['2010-2017'] = data_df['2017']/data_df['2010']
data_df['1990-2000'] = (data_df['1990-2000']-1.0)*100.0
data_df['2000-2010'] = (data_df['2000-2010']-1.0)*100.0
data_df['2010-2017'] = (data_df['2010-2017']-1.0)*100.0

del data_df['1990']
del data_df['2000']
del data_df['2010']
del data_df['2017']

values = ['New York - Newark - Jersey City', 'Chicago - Naperville - Elgin', 'Los Angeles - Long Beach - Anaheim', 'San Francisco - Oakland - Hayward']

red_data = data_df[data_df['area_name'].isin(values)]
red_data.plot.bar(x='area_name')

plt.xticks([0,1,2,3],['Chicago', 'Los Angeles', 'New York','San Francisco'])
plt.tight_layout()
plt.title('Population Increase Percentage Over Time')
plt.ylabel('Population Change %')
plt.xlabel('Area Name')
file_name = file_dir + '/percentage_change.pdf'
plt.savefig(file_name)
