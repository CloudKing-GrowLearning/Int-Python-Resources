from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.citypopulation.de/UK-Cities.html'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

country_table = html_soup.find('table', id='tl')
table_rows = country_table.find_all('tr')

heading_list = []
name = []
pop_1991 = []
pop_2001 = []
pop_2011 = []
pop_2016 = []

for row in table_rows:
   heading = row.find_all('th')
   cells = row.find_all('td')
   if len(heading)== 12:
       for x in range(0, len(heading)):
           heading_list.append(heading[x].find(text=True))
   if len(cells) == 12:
       for c in cells:
           print(c)
       pref_name = cells[1].find(text=True)
       name.append(pref_name)

       pop1991 = cells[6].find(text=True)
       pop_1991.append(pop1991)

       pop2001 = cells[7].find(text=True)
       pop_2001.append(pop2001)

       pop2011 = cells[8].find(text=True)
       pop_2011.append(pop2011)

       pop2016 = cells[9].find(text=True)
       pop_2016.append(pop2016)


df = pd.DataFrame({heading_list[1] : name,
                  '1991': pop_1991,
                  '2001' : pop_2001,
                  '2011' : pop_2011,
                  '2016' : pop_2016,
                 })

file_name = 'uk_data.csv'
df.to_csv(file_name, index=False)