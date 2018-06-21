from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.citypopulation.de/Japan-Cities.html'
url2 = ''#http://www.stat.go.jp/english/data/index.html

response = get(url)
#print(response.text)

html_soup = BeautifulSoup(response.text, 'html.parser')
#print(type(html_soup))

country_table = html_soup.find('table', id='tl')
#print(type(country_table))
#print(len(country_table))
table_rows = country_table.find_all('tr')
#print(len(table_rows))

heading_list = []
name = []
pop_1995 = []
pop_2000 = []
pop_2005 = []
pop_2010 = []
pop_2015 = []
for row in table_rows:
    heading = row.find_all('th')
    cells = row.find_all('td')
    #print(len(heading))
    if len(heading)== 15:
        for x in range(0, len(heading)):
            heading_list.append(heading[x].find(text=True))
            #heading_list.append(heading[x].find_all(text=True))
    if len(cells) == 15:
        pref_name = cells[1].find(text=True)
        name.append(pref_name)

        pop1995 = cells[8].find(text=True)
        pop_1995.append(pop1995)

        pop2000 = cells[9].find(text=True)
        pop_2000.append(pop2000)

        pop2005 = cells[10].find(text=True)
        pop_2005.append(pop2005)

        pop2010 = cells[11].find(text=True)
        pop_2010.append(pop2010)

        pop2015 = cells[12].find(text=True)
        pop_2015.append(pop2015)
#print(heading_list)
#print(name)
#print(pop_1995)
#print(pop_2000)
#print(pop_2005)
#print(pop_2010)
print(pop_2015)

df = pd.DataFrame({heading_list[1] : name,
                   '1995': pop_1995,
                   '2000' : pop_2000,
                   '2005' : pop_2005,
                   '2010' : pop_2010,
                   '2015': pop_2015})

df.to_csv('popOutput.csv')