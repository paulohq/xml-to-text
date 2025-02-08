# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
# https://realpython.com/python-xml-parser/

import sys
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


#tree = ET.parse('fruits.xml')
#root = tree.getroot()

#for element in root.findall('name'):
#    print(element.text)



# Reading the data inside the xml
# file to a variable under the name
# data
def load_xml(path):

    with open(path, 'r') as f:
        data = f.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        Bs_data = BeautifulSoup(data, "xml")

        # Finding all instances of tag
        # `unique`
        b_unique = Bs_data.find_all('dezembro')

        print(b_unique)

        # Using find() to extract attributes
        # of the first instance of the tag
        b_name = Bs_data.find('dezembro', {'despesas':'469,30'})

        print('despesas: ' + str(b_name))

        # Extracting the data stored in a
        # specific attribute of the
        # `child` tag
        mes = b_name.get('mes')
        despesa = b_name.get('despesas')

        print('Mes: ' + mes)
        print('despesas: ' + despesa)

        consolidacao = Bs_data.find_all('consolidacao')
        print(consolidacao)

def main(file):
    load_xml(file)
   # extract()

if __name__ == "__main__":
    main(sys.argv[1])