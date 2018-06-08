import json, urllib
import requests

with urllib.request.urlopen("https://grow-learning-dc-test.000webhostapp.com/country.json") as url:
    data = json.load(url)

    for c in data['country']:
        #print('Name: ' + c['name'])
        for ruler in c['ruler']:
            if ruler['resign_start'] == '1449':
                print('Name: ' + ruler['name'])
