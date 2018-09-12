import os
from lxml import objectify
import pandas as pd
import matplotlib.pyplot as plt

file_dir = os.getcwd()
file = file_dir + '/Race-Of-Alleged-Victims-Compared-To-New-York-City.xml'
xml = objectify.parse(open(file))

root = xml.getroot()

print(len(root.getchildren()[0].getchildren()))

df = pd.DataFrame(columns=('Race', '2005', '2006', '2007', '2008', '2009'))
for i in range(0, len(root.getchildren()[0].getchildren())):
    row = root.getchildren()[0].getchildren()[i].getchildren()
    row_num = len(row)
    race = root.getchildren()[0].getchildren()[i].getchildren()[0].text
    print(race)
    if row_num == 13:
        row_dict = dict(zip(['Race', '2005', '2006', '2007', '2008', '2009'], [row[0].text, row[1].text, row[3].text, row[5].text, row[7].text, row[9].text]))
        row_s = pd.Series(row_dict)
        row_s.name = i
        df = df.append(row_s)
    #elif row_num == 7:
print(df.head())
print(df['Race'].tolist())
race_list = df['Race'].tolist()[:4]
# Create a pie chart
colors = ['yellowgreen', 'gold', 'lightsalmon', 'darkred']
plt.pie(
    # using data total)arrests
    df['2009'][:4],#maybe question
    # with the labels being officer names
    labels=race_list,
    # with no shadows
    shadow=True,
    # with colors
    colors=colors,
    # with one slide exploded out
    explode=(0.15, 0, 0, 0),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%'
    )

# View the plot drop above
plt.axis('equal')
plt.title('Unemployment of people with advanced eduction % (2016)')
# View the plot
plt.tight_layout()
plt.legend()
plt.savefig(file_dir + '/Race-Of-Alleged-Victims-Compared-To-New-York-City-pie.pdf')