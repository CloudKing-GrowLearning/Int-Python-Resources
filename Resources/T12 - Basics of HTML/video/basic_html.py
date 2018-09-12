import pandas as pd
import os

dir = os.getcwd()
file_name = dir + '/world_data_bank.csv'
data = pd.read_csv(file_name, sep=';')

reduced_data = data[['Indicator Name','2013','2014','2015','2016']]

values = ['Unemployment with intermediate education (% of total labor force with intermediate education)',
          'Unemployment with intermediate education, male (% of male labor force with intermediate education)',
          'Unemployment with intermediate education, female (% of female labor force with intermediate education)']

reduced_data = reduced_data[reduced_data['Indicator Name'].isin(values)]

print(reduced_data)

file_name = dir + '/world_data_bank.html'
fo = open(file_name, 'w')
fo.write(reduced_data.to_html())
fo.close()