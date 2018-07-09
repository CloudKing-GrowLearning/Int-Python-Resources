#This is probably pretty similar to what we have done in the intro course but here I show how you can customise
#the chart using plt and save it directly to file
import pandas as pd
import matplotlib.pyplot as plt

file_name = 'some_file_path'
data = pd.read_csv(file_name)
data.plot.scatter('some_column_name','some_other_column_name')
plt.title('A title')
plt.xlabel('Some text')
plt.ylabel('Some other text')
plt.savefig('path_to_file')

#Do we have a specific example that we want to use for this on the data or do you want me to do another example