import pandas as pd
import os

file_dir = os.getcwd()
file_name = file_dir + '/sat_data.csv'
data = pd.read_csv(file_name)

data = data[data['sat_math_avg_score'] != 's']
data = data[data['sat_critical_reading_avg_score'] != 's']
data = data[data['sat_writing_avg_score'] != 's']

data['sat_math_avg_score'] = data['sat_math_avg_score'].astype('float')
data['sat_critical_reading_avg_score'] = data['sat_critical_reading_avg_score'].astype('float')
data['sat_writing_avg_score'] = data['sat_writing_avg_score'].astype('float')
data['num_of_sat_test_takers'] = data['num_of_sat_test_takers'].astype('int')

data.reset_index()
data.index = data['school_name']
data = data.sort_values('sat_math_avg_score', ascending=False)

reduced_data = data[['sat_math_avg_score', 'sat_critical_reading_avg_score', 'sat_writing_avg_score']].head(10)

file_name =  file_dir + '/sat_data.html'
fo = open(file_name, 'w')
fo.write(reduced_data.to_html())
fo.close()
