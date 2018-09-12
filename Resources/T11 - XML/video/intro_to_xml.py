from urllib.request import urlopen
import os
from lxml import objectify
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://health.data.ny.gov/api/views/pv2d-3398/rows.xml?accessType=DOWNLOAD'
response = urlopen(url)
data = response.read()
data  = data.decode()

file_dir = os.getcwd()
file_name = file_dir + '/health_data.xml'
fo = open(file_name, 'w')
fo.write(data)
fo.close()

xml =objectify.parse(open(file_name))
root = xml.getroot()

cdc_week = []
week_ending_date =[]
season = []
total_influenza_reported = []
influenza_a = []
influenza_b = []
influenza_type_not_specified = []
row_id = []

children = root.row.getchildren()
for child in children:
    cdc_week.append(int(child.cdc_week.text))
    week_ending_date.append(pd.to_datetime(child.week_ending_date.text))
    season.append(child.season.text)
    total_influenza_reported.append(int(child.total_influenza_reported.text))
    influenza_a.append(int(child.influenza_a.text))
    influenza_b.append(int(child.influenza_a.text))
    influenza_type_not_specified.append(int(child.influenza_type_not_specified.text))
    row_id.append(int(child.row_id.text))

data_dict = {}
data_dict['cdc_week'] = cdc_week
data_dict['week_ending_date'] = week_ending_date
data_dict['season'] = season
data_dict['total_influenza_reported'] = total_influenza_reported
data_dict['influenza_a'] = influenza_a
data_dict['influenza_b'] = influenza_b
data_dict['influenza_type_not_specified'] = influenza_type_not_specified
data_dict['row_id'] = row_id
data_df = pd.DataFrame(data_dict)

data_df.plot.line('week_ending_date', 'total_influenza_reported', legend=False)
plt.title('Total Influenza Reported Over Time')
plt.xlabel('Week Ending Date')
plt.ylabel('Total Influenza Reported')
file_name = file_dir + '/total_influenza.pdf'
plt.savefig(file_name)



