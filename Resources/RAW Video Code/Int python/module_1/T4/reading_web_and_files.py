from urllib.request import urlopen
import os

url = 'https://classroom.sagepub.com/pluginfile.php/2500/course/section/976/world_data_bank.csv'
response = urlopen(url)
data = response.read()
type(data)
data = data.decode()

file_dir = os.getcwd()
file_name = file_dir + '/world_data_bank.csv'
fo = open(file_name, 'w')
fo.write(data)
fo.close()

f = open(file_name, 'r')
data = f.read()
print(data)
