import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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
employment_data_transform.index = employment_data.index.astype(int)
employment_data_transform.plot()
plt.title('Unemployment of people with advanced eduction %')
plt.xlabel('Year')
plt.ylabel('Percent Growth')
plt.savefig(file_dir + '/Unemployment_advanced_eduction.pdf')

# Create a pie chart
plt.pie(
    # using data total)arrests
    employment_data['2016'],
    # with the labels being officer names
    labels=['Male', 'Female'],
    # with no shadows
    shadow=False,
    # with colors
    #colors=colors,
    # with one slide exploded out
    #explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%'
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.savefig(file_dir + '/Unemployment_advanced_eduction_pie_example.pdf')

print(employment_data.columns.values)
print(list(employment_data))
print(employment_data.index)

employment_data = employment_data.dropna(axis='columns')

print(len(employment_data.columns))
# Create Plot
fig, ax = plt.subplots()
index = np.arange(len(employment_data.columns))
bar_width = 0.35
opacity = 0.8

#employment_data = employment_data.dropna(axis='columns')

rects1 = plt.bar(index, list(employment_data.iloc[0]), bar_width,
                 color='r',
                 label='Male')

rect2 = plt.bar(index + bar_width, list(employment_data.iloc[1]), bar_width,
                color='g',
                label='Female')

plt.xlabel('Year')
plt.ylabel('Percentage %')
plt.title('Unemployment of people with advanced eduction %')
plt.xticks(index + (bar_width/2), list(employment_data), rotation='vertical')
plt.legend()

plt.grid()
plt.tight_layout()
plt.savefig(file_dir + '/Unemployment_advanced_eduction_bar_example2.pdf')