import pandas as pd
import os
import T3_Functions_Scripts.ga_complete.Lib as cm

file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'

data = pd.read_csv(file_name, sep=';')
print(data.iloc[:5]['Indicator Name'])
print(data.iloc[8]['2016'])

df = pd.DataFrame()
df = df.append(data.iloc[9:11])

print(df.head())
print(df[['2010','2016']].describe())

employment_data = data.iloc[[9, 10]]
del employment_data['Country Name']
del employment_data['Country Code']
del employment_data['Indicator Name']
del employment_data['Indicator Code']

print(cm.compare(employment_data.iloc[0]['2015'], employment_data.iloc[1]['2015']))
print(employment_data.iloc[1]['2015'])
