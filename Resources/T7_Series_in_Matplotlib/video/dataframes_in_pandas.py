import pandas as pd
import os

file_dir = os.getcwd()
file_name  = file_dir + '/world_data_bank.csv'

data = pd.read_csv(file_name, sep=';')
print(data[['2010','2011']].describe())