from lxml import objectify
import pandas as pd

path_file = 'movies.xml'
xml = objectify.parse(open(path_file))

root = xml.getroot()

df = pd.DataFrame(columns=('title', 'release', 'run_time', 'genre', 'age_rating', 'description'))
for i in range(0, len(root.getchildren())):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['title', 'release', 'run_time', 'genre', 'age_rating', 'description'], [obj[0].text, obj[1].text, obj[2].text, obj[3].text, obj[4].text, obj[5].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)


df.to_csv('out.csv')

