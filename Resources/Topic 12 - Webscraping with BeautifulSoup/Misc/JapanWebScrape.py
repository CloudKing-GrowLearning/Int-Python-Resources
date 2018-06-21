#import the library used to query a website
from urllib.request import urlopen
#import the BeautifulSoup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#import pandas to convert list to data frame
import pandas as pd

#specify the url
wiki = "https://en.wikipedia.org/wiki/Prefectures_of_Japan"

#Attempt to open the url and return an Request as a variable 'page'
page = urlopen(wiki)

#Parse the html in the page variable, and store it in BeautifulSoup format
#soup = BeautifulSoup(page)#UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml").
# This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
soup = BeautifulSoup(page, "lxml")

#print(soup.prettify())
#print(soup.title.string)
#all_table = soup.find_all('table')
#print(all_table)

right_table = soup.find('table', {"class": 'wikitable sortable'})
#print(right_table)

#
heading_list = []
data_dict = {}
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
I = []
J = []
K = []
L = []
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    heading = row.findAll('th')
    if len(heading)== 12:
        for x in range(0, len(heading)):
            heading_list.append(heading[x].find(text=True))

    if len(cells) == 12:
        #for i in range(0, len(cells)):
            #row_list = []
            #row_list.append(cells[i].find(text=True))
            #if i == 1:
                #A.append(cells[1].find(text=True))
            #print(cells[i].find(text=True))
            #print(row_list)
        #row_list = []
        #for i in range(0, len(cells)):
            #row_list.append(cells[i].find(text=True))
            #print(row_list)
            #data_dict[i] = row_list
            #print(data_dict.values())
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[5].find(text=True))
        G.append(cells[6].find(text=True))
        H.append(cells[7].find(text=True))
        I.append(cells[8].find(text=True))
        J.append(cells[9].find(text=True))
        K.append(cells[10].find(text=True))
        L.append(cells[11].find(text=True))

df = pd.DataFrame(A, columns=[heading_list[0]])
#for i in range(1, 12):
    #col_head = heading_list[i]
    #print(col_head)
    #df[col_head] = B

df[heading_list[1]] = B
df[heading_list[2]] = C
df[heading_list[3]] = D
df[heading_list[4]] = E
df[heading_list[5]] = F
df[heading_list[6]] = G
df[heading_list[7]] = H
df[heading_list[8]] = I
df[heading_list[9]] = J
df[heading_list[10]] = K
df[heading_list[11]] = L

df.to_csv('output.csv')

#Next step maybe connect to googlemaps?