import pandas as pd
import matplotlib.pyplot as plt

file_name = 'some_file_path'
data = pd.read_csv(file_name)

column_data = data['some_column_name']
column_data.hist()
plt.title('A title')
plt.xlabel('Some text')
plt.ylabel('Some other text')
plt.savefig('path_to_file')

#Do we want more examples? And what specifically should we show from the dataset