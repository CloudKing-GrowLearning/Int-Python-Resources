import pandas as pd
file_name = 'some_file_path'
data = pd.read_csv(file_name)
#Access the dataframe by column
data['some_column_name']
#Access by a few column name
data[['one_colum_name', 'another_column_name']]
#Access row by index
data[some_index_value]
#Access splice of collumn(s)
data['some_column_name'][1:6]
data[['one_colum_name', 'another_column_name']][1:6]
#Show you can use negative indexing
data['some_column_name'][-6:-1]
data[['one_colum_name', 'another_column_name']][-6:-1]
#Discuss how a single column is just a series and show how methods can be applied across multiple columns
data[['one_colum_name', 'another_column_name']].mean()
data[['one_colum_name', 'another_column_name']].sum()
data[['one_colum_name', 'another_column_name']].std()
data[['one_colum_name', 'another_column_name']].describe()
#Do we have a specific question to answer?