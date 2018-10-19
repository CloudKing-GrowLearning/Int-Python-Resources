import json
from urllib.request import urlopen

with urlopen("https://classroom.sagepub.com/pluginfile.php/3016/mod_resource/content/0/old_civilizations.json") as url:
    data = json.load(url)

    for c in data['civilizations']:
        for ruler in c['ruler']:
            if ruler['reign_start'] == '1449':
                print('Name: ' + ruler['name'])
