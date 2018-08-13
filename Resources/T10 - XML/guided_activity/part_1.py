from lxml import objectify
import pandas as pd

path_file = 'book.xml'
xml = objectify.parse(open(path_file))

root = xml.getroot()
print(root.getchildren()[8].getchildren()[1])