#Here we are going to read the file in using the open method

import pandas as pd
file_name = 'some_file_path'
f = open(file_name, 'r')
data = f.read()
data = data.split('\n')
headers = data[0].split(',')
data = data[1:]

#So this will be a list of some column that we will turn into a series this needs to be decided
some_column = []

for d in data:
    row = d.split(',')
    row_dict = dict(zip(headers, row))
    value = row_dict['some_column_name']
    some_column.append(value)

#We then convert the list into a series and can look at some stats and how to access different elements in it
some_column_series = pd.Series(some_column)
#Show how we can access certain elemnts using index
some_column_series.index
some_column_series[12]
#Show how we can use standard list access approach on the series
some_column_series[1:6]
#And negative indexing
some_column_series[-6:-1]
#And the third argument
some_column_series[-6:-1:2]
#Then show some methods that we can apply to a series
some_column_series.mean()
some_column_series.sum()
some_column_series.std()
some_column_series.describe()