from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'http://www.citypopulation.de/php/usa-metro.php'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

country_table = html_soup.find('table', id='ts')
table_rows = country_table.find_all('tr')

heading_list = []
name_list = []
status_list = []
state_list = []
pop_1990_list = []
pop_2000_list = []
pop_2010_list = []
pop_2017_list = []

for row in table_rows:
    heading = row.find_all('th')
    cells = row.find_all('td')
    if len(heading) == 8:
        for x in range(0, len(heading) - 1):
            heading_list.append(heading[x].find(text=True))
    if len(cells) == 8:
        name = cells[0].find(text=True)
        name_list.append(name)

        status = cells[1].find(text=True)
        status_list.append(status)

        state = cells[2].find(text=True)
        state_list.append(state)

        pop_1990 = cells[3].find(text=True).replace(',','')
        pop_1990_list.append(int(pop_1990))

        pop_2000 = cells[4].find(text=True).replace(',','')
        pop_2000_list.append(int(pop_2000))

        pop_2010 = cells[5].find(text=True).replace(',','')
        pop_2010_list.append(int(pop_2010))

        pop_2017 = cells[6].find(text=True).replace(',','')
        pop_2017_list.append(int(pop_2017))

data_df = pd.DataFrame({'area_name' : name_list,
                        'status': status_list,
                        'state': state_list,
                        '1990' : pop_1990_list,
                        '2000' : pop_2000_list,
                        '2010': pop_2010_list,
                        '2017': pop_2017_list})

data_df = data_df[['area_name','status','state','1990','2000','2010','2017']]
print(data_df.head())
file_dir = os.getcwd()
file_name = file_dir + '/met_areas.csv'
data_df.to_csv(file_name, index=False)

