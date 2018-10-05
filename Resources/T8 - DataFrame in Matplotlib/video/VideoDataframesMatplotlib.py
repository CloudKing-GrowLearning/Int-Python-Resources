import pandas as pd
import os
import matplotlib.pyplot as plt

file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'

data = pd.read_csv(file_name, sep=';')

population_data = data.iloc[[614, 616]]
del population_data['Country Name']
del population_data['Country Code']
del population_data['Indicator Name']
del population_data['Indicator Code']

population_data_transform = population_data.T
population_data_transform.columns = ['Urban', 'Rural']
population_data_transform.index = population_data_transform.index.astype(int)
population_data_transform.plot()
plt.title('Population Growth %')
plt.xlabel('Year')
plt.ylabel('Percent Growth')
plt.savefig(file_dir + '/population_growth.pdf')
