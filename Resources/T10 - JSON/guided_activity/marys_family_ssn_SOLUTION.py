import json

#with open('country.json') as json_file:
    #data = json.load(json_file)
    #for c in data['country']:
    #    print('Name: ' + c['name'])
     #   print('')

with open('Marys_family_ssn.json') as js:
    j = json.load(js)
    print(type(j))

    for items in j['family']['kids']:
        if '1234' in items['ssn']:
            print(items['name'])