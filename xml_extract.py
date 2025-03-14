# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
# https://realpython.com/python-xml-parser/

import sys
import os
from bs4 import BeautifulSoup
import xml.dom.minidom as md

#import xml.etree.ElementTree as ET
from lxml import etree as ET

XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
<States>
    <state name ="TELANGANA">
        <rank>1</rank>
        <neighbor name ="ANDHRA" language ="Telugu"/>
        <neighbor name ="KARNATAKA" language ="Kannada"/>
    </state>
    <state name ="GUJARAT">
        <rank>2</rank>
        <neighbor name ="RAJASTHAN" direction ="N"/>
        <neighbor name ="MADHYA PRADESH" direction ="E"/>
    </state>
    <state name ="KERALA">
        <rank>3</rank>
        <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
    </state>
</States>
'''



#tree = ET.parse('fruits.xml')
#root = tree.getroot()

#for element in root.findall('name'):
#    print(element.text)



# Reading the data inside the xml
# file to a variable under the name data
def load_xml(path):

    with open(path, 'r') as f:
        data = f.read()

        # Passing the stored data inside
        # the beautifulsoup parser, storing
        # the returned object
        Bs_data = BeautifulSoup(data, "lxml-xml")

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

def extract():
    # parsing from the string.
    root = ET.fromstring(XMLexample_stored_in_a_string)
    # printing attributes of the root tags 'neighbor'.
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)
    # finding the state tag and their child attributes.
    for state in root.findall('state'):
        rank = state.find('rank').text
        name = state.get('name')
        print(name, rank)

def insert_update_AR(file):
    tree = ET.parse(file)
    root = tree.getroot()

    # itera sobre os elementos do root.
    for child in root:
        # se a tag do nó for igual a escrituracao
        if child.tag == 'escrituracao':
            #itera sobre os filhos do nó escrituração.
            for c in child.getchildren():
                if c.tag != 'colecaoPlanoContas':
                    print(c.attrib)
                    for l in c.iterchildren():
                        print(l)
            print('aqui')
        print(child.tag)

    for el in root.iter():
        print(el.tag)

    # itera sobre o terceiro elemento abaixo do nó root (escrituracao).
    for child in root[2]:
        # se a tag do nó for diferente de colecaoPlanoContas (tags dos meses).
        if child.tag != 'colecaoPlanoContas':
            # soma valor ao saldo do item.
            vl = float(child.attrib.values()[1].replace(',','.')) + float("10,80".replace(',','.'))
            # converte para decimal com dois dígitos.
            vl1 = f'{vl:,.2f}'
            # substitui "." por "," e grava no campo saldo do item.
            child.set('saldo', vl1.replace('.',','))

    #mes = root.xpath("/dezembro")
    #item = root.xpath("//escrituracao/dezembro/item")
    # itera sobre os itens do mês 12
    for item in root[2][12].iter('item'):
        item.set('valor', '100,30')
        # soma valor ao item.
        vl = float(item.attrib.values()[6].replace(',','.')) + float("10,80".replace(',','.'))
        # converte para decimal com dois dígitos.
        vl1 = f'{vl:,.2f}'
        # substitui "." por "," e grava no valor do item.
        item.set('valor', vl1.replace('.',','))

    # adiciona nó item no mês 12.
    element = ET.SubElement(root[2][12], 'item')
    # adiciona as tags no elemento adicionado acima.
    element.set('classificacaoConta', '')
    element.set('codTipoContaSelecao', '2.23.004')
    element.set('data', '14/03/2025')
    element.set('historico', 'COMPRA DE COMBUSTIVEL DA CIA BRASILEIRA DE DISTRIBUICAO CNPJ 47.508.411/0786-94 NF 729057 SE 302')
    element.set('nomeAbaConta', "DEZ")
    element.set('pais', "105")
    element.set('valor', "120,53")

    t = element.getroottree()
    print(t.getroot().tag)
    for month in root.iter('dezembro'):
        print(month.attrib.items())
        print(month.attrib.values())

    tree.write('xml/AR-output.xml')
def insert_update():
    # https://www.geeksforgeeks.org/modify-xml-files-with-python/
    mytree = ET.parse('xml/document.xml')
    myroot = mytree.getroot()
    # iterating through the price values.
    for prices in myroot.iter('price'):
        # updates the price value
        prices.text = str(float(prices.text) + 10)
        # creates a new attribute
        prices.set('newprices', 'yes')

    # creating a new tag under the parent.
    # myroot[0] here is the first food tag.
    ET.SubElement(myroot[0], 'tasty')
    for temp in myroot.iter('tasty'):
        # giving the value as Yes.
        temp.text = str('YES')

    # deleting attributes in the xml.
    # by using pop as attrib returns dictionary.
    # removes the itemid attribute in the name tag of
    # the second food tag.
    myroot[1][0].attrib.pop('itemid')
    myroot[1][2].attrib.pop('teste')

    # Removing the tag completely we use remove function.
    # completely removes the third food tag.
    myroot.remove(myroot[2])

    mytree.write('output.xml')

def parse_xml():
    # https://www.geeksforgeeks.org/how-to-parse-and-modify-xml-in-python/?ref=ml_lbp
    # parsing the xml file and
    # storing the contents in
    # "file" object Put in the
    # path of your XML file in
    # the parameter for parse() method.
    file = md.parse("xml/soccer.xml")

    # nodeName returns the type of
    # the file(in our case it returns
    # document)
    print(file.nodeName)

    # firstChild.tagName returns the
    # name of the first tag.Here it
    # is "note"
    print(file.firstChild.tagName)

    firstname = file.getElementsByTagName("fname")

    # printing the first name
    print("Name: " + firstname[0].firstChild.nodeValue)

    lastname = file.getElementsByTagName("lname")

    # printing the last name
    print("Surname: " + lastname[0].firstChild.nodeValue)

    favgame = file.getElementsByTagName("favgame")

    # printing the favourite game
    print("Favourite Game: " + favgame[0].firstChild.nodeValue)

    # Printing tag values having
    # attributes(Here tag "player"
    # has "name" attribute)
    players = file.getElementsByTagName("player")

    for player in players:
        print(player.getAttribute("name"))

def main(file):
    insert_update_AR(file)
    #load_xml(file)
    #extract()
    #insert_update()
    #parse_xml()

if __name__ == "__main__":
    main(sys.argv[1])
