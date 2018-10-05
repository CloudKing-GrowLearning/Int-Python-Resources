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

print(employment_data.columns.values)
print(list(employment_data))
print(employment_data.index)

employment_data = employment_data.dropna(axis='columns')

print(len(employment_data.columns))
# Create Plot
fig, ax = plt.subplots()
index = pd.Series(range(len(employment_data.columns)))
bar_width = 0.35
opacity = 0.8


rects1 = plt.bar(index, list(employment_data.iloc[0]), bar_width,
                 color='b',
                 label='Male')

rect2 = plt.bar(index + bar_width, list(employment_data.iloc[1]), bar_width,
                color='r',
                label='Female')

plt.xlabel('Year')
plt.ylabel('Percentage %')
plt.title('Unemployment of people with advanced education %')
plt.xticks(index + (bar_width/2), list(employment_data), rotation='vertical')
plt.legend()

#plt.grid()
plt.tight_layout()
plt.savefig(file_dir + '/Unemployment_advanced_eduction_bar_example.pdf')