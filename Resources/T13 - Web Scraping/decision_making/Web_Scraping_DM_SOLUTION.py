from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

import os

file_dir = os.getcwd()

#First page Scrape
url = 'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2015'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

country_table = html_soup.find('table', id='t2')
table_rows = country_table.find_all('tr')

dict_coli = {'country': [], 'coli': []}
for row in table_rows:
    cells = row.find_all('td')
    if len(cells) == 8:
        country = cells[1].find(text=True)
        dict_coli['country'].append(country)

        cost_of_liv_index = cells[2].find(text=True)
        dict_coli['coli'].append(cost_of_liv_index)

df = pd.DataFrame.from_dict(dict_coli)
df = df[['country', 'coli']] #Change the order or could use OrderedDict

#Second Page scrape
url2 = 'https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy'

response2 = get(url2)

html_soup2 = BeautifulSoup(response2.text, 'html.parser')

country_table_list = html_soup2.find_all('table', class_='wikitable sortable')

table_rows2 = country_table_list[3].find_all('tr')

dict_le = {'country': [], 'le': []}

for row in table_rows2:
    cells = row.find_all('td')
    if len(cells) == 5:
        country = cells[1].find('a')['title']
        dict_le['country'].append(country)

        life_exp = cells[2].find(text=True)
        dict_le['le'].append(life_exp)

df2 = pd.DataFrame.from_dict(dict_le)
df2 = df2[['country', 'le']] #Change the order or could use OrderedDict

#Plot Creation
fin_df = pd.merge(df, df2, on='country')
fin_df = fin_df.rename(columns = {'coli':'cost of living index'})
fin_df = fin_df.rename(columns = {'le':'life expectancy'})


num_rate = 5
coli_list = fin_df['cost of living index'][:num_rate]
le_list = fin_df['life expectancy'][:num_rate]
country_list = fin_df['country'][:num_rate]

for i in range(0, num_rate):
      coli_list[i] = float(coli_list[i])
      le_list[i] = float(le_list[i])

#Create Plot
fig, ax = plt.subplots()
index = pd.Series(range(num_rate))
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, coli_list, bar_width,
                alpha=opacity,
                color='r',
                label='cost of living index')

rect2 = plt.bar(index + bar_width, le_list, bar_width,
                alpha=opacity,
                color='b',
                label='life expectancy')

plt.xlabel('Country')
plt.ylabel('cost of living/life expectancy')
plt.title('Comparison of Life Expectancy and cost of living across countries')
plt.xticks(index + (bar_width / 2), country_list, rotation='vertical')
plt.legend()

plt.tight_layout()
#plt.show()
plt.savefig(file_dir + '/cost_of_living_against_life_expect.png')