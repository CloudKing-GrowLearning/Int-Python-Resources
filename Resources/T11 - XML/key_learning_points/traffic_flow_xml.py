from urllib.request import urlopen
import os
from lxml import objectify
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://data.seattle.gov/api/views/38vd-gytv/rows.xml?accessType=DOWNLOAD'

response = urlopen(url)
data = response.read()
type(data)
data = data.decode()

file_dir = os.getcwd()
file_name = file_dir + '/traffic_flow_map_volumes.xml'
fo = open(file_name, 'w')
fo.write(data)
fo.close()

xml = objectify.parse(open(file_name))
root = xml.getroot()

children = root.row.getchildren()

header = ['objectid','stname','count_location','year','segkey','aawdt','input_study_id']
child_list = []
for c in children:
   row = c.getchildren()
   row_dict = dict(zip(header, row))
   child_list.append(row_dict)

data_df = pd.DataFrame(child_list)
data_df.to_csv(file_dir + '/traffic_flow_map_volumns.csv', index=False)

value_counts = data_df['stname'].value_counts().head(10)

value_counts.plot.bar()
plt.title("Value counts of street names in Seattle")
plt.xlabel("Street names")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(file_dir + '/traffic_flow_map_volumns.png')