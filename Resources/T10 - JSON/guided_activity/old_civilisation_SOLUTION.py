import json, urllib
from urllib.request import urlopen

with urlopen("https://grow-learning-dc-test.000webhostapp.com/country.json") as url:
    data = json.load(url)

    for c in data['country']:
        #print('Name: ' + c['name'])
        for ruler in c['ruler']:
            if ruler['reign_start'] == '1449':
                print('Name: ' + ruler['name'])
