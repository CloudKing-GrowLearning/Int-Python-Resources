import pandas as pd
import os
import matplotlib.pyplot as plt


file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'

data = pd.read_csv(file_name, sep=';')

employment_data = data.iloc[[9, 10]]
del employment_data['Country Name']
del employment_data['Country Code']
del employment_data['Indicator Name']
del employment_data['Indicator Code']


employment_data_transform = employment_data.T
employment_data_transform.columns = ['Male', 'Female']
employment_data_transform.index= employment_data_transform.index.astype(int)
employment_data_transform.plot()
plt.title('Unemployment of people with advanced education %')
plt.xlabel('Year')
plt.ylabel('Percent Growth')
plt.savefig(file_dir + '/Unemployment_advanced_education.pdf')