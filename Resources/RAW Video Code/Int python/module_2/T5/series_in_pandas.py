import pandas as pd
import os

file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'

f = open(file_name, 'r')
data = f.read()
data = data.split('\n')
data.pop()
headers = data[0].split(';')
data = data[1:]

initial_year = 1960
year_list = []
for x in range(58):
    year = initial_year + x
    year_list.append(year)

female = []

for d in data:
    row = d.split(';')
    row_dict = dict(zip(headers, row))
    if row_dict['Indicator Name'] == 'Share of youth not in education, employment or training, female (% of female youth population)':
        for year in year_list:
            value = row_dict[str(year)]
            if value == '':
                value = None
                female.append(value)
            else:
                female.append(float(value))

female_series = pd.Series(female)
female_series.index = year_list
print(female_series[2016])