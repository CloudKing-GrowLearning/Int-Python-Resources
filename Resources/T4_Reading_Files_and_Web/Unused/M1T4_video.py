#This is basically the same code from the introduction course, we cant do much else here

from urllib.request import urlopen

url = 'some_url'
response = urlopen(url)
data = response.read()
type(data)
data = data.decode()

file_name = '/Users/rob/Desktop/urlresults.csv'
fo = open(file_name, 'w')
fo.write(data)
fo.close()