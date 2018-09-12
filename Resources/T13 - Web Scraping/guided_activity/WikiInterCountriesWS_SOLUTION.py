from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

country_table = html_soup.find('table', class_='wikitable sortable')

table_rows = country_table.find_all('tr')

heading_list = []
country = []
internet_users = []
user_rank = []
percentage = []
percentage_rank = []
for row in table_rows:
    cells = row.find_all('td')
    heading = row.find_all('th')

    if len(heading)== 5:
        for x in range(0, len(heading)):
            heading_list.append(heading[x].find(text=True))

    if len(cells) == 5:
        cou = cells[0].a.find(text=True)
        country.append(cou)

        iu = cells[1].find(text=True)
        internet_users.append(iu)

        ur = cells[2].find(text=True)
        user_rank.append(ur)

        per = cells[3].find(text=True)
        percentage.append(per)

        pr = cells[4].find(text=True)
        percentage_rank.append(pr)


df = pd.DataFrame({heading_list[0]: country,
                   heading_list[1]: internet_users,
                   heading_list[2]: user_rank,
                   heading_list[3]: percentage,
                   heading_list[4]: percentage_rank
                   })
print(percentage_rank)