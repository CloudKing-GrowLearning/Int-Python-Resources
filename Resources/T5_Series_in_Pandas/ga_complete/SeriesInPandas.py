import pandas as pd
import os
import matplotlib.pyplot as plt

file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'

f = open(file_name, 'r')
data = f.read()
data = data.split('\n\n')#weird format issue
data.pop()
#print(data)
headers = data[0].split(';')
data = data[1:]
#print(data)

initial_year = 1960
year_list = []
for x in range(58):
    year = initial_year + x
    year_list.append(year)

male = []

for d in data:
    row = d.split(';')
    row_dict = dict(zip(headers, row))
    if row_dict['Indicator Name'] == 'Share of youth not in education, employment or training, male (% of male youth population)':
        for year in year_list:
            value = row_dict[str(year)]
            if value == '':
                value = None
                male.append(value)
            else:
                male.append(float(value))

print(male[53])

male_series = pd.Series(male)
male_series.index = year_list
#print(male_series[2016])
print(male_series)
print(male_series.nsmallest(4))
print(male_series.nlargest(4))
male_series = male_series.dropna()
male_series.plot(kind='barh')
plt.title('Youth not in employment (Bar Chart)')
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.grid()
plt.savefig(file_dir + '/barh_example.pdf')
