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
plt.title('Unemployment of people with advanced education % (2016)')
# View the plot
plt.tight_layout()
plt.savefig(file_dir + '/Unemployment_advanced_education_pie_example.pdf')