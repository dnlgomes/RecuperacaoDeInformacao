#!/usr/bin/python
# coding: utf8
import re
import xml.etree.ElementTree as ET
from collections import Counter

# file = open("ptwiki-v2.trec")
#
# text = file.read(10000)



#for child in root:
#    print(child[0].tag, child[0].text)

def tratarTextoTree(text):
    text = re.sub("&.{2,4};", " ", text)
    text = re.sub("\\{\\{!\\}\\}", " ", text)
    # Remove text in the format {{ ... }}
    text = re.sub("{{.*?}}", "", text)
    # Remove markup tags in the format <foo> OR </foo>
    text = re.sub("<.*?>", "", text)

    text = tratarTexto(text)
    text = re.sub(r'\s+', ' ', text).strip()# substituir espaços em branco grandes por um whitespace

    # remove all non alphanumeric characters
    return text


def tratar(text):
    #text to lowercase and remove white trailing spaces
    text = text.lower().strip()
    text = re.sub("&.{2,4};", " ", text)
    text = re.sub("\\{\\{!\\}\\}", " ", text)
    # Remove text in the format {{ ... }}
    text = re.sub("{{.*?}}", "", text)
    # Remove markup tags in the format <foo> OR </foo>
    text = re.sub("<.*?>", "", text)
    # remove all non alphanumeric characters
    text = re.sub("[\[\]\|\,\.\;\:\'\"()]", " ", text)
    text = re.sub(r'\s+', ' ', text).strip()# substituir espaços em branco grandes por um whitespace
    return text

def tratar2(text):
    text = re.sub("\\{\\{!\\}\\}", " ", text)
    # Remove text in the format {{ ... }}
    text = re.sub("{{.*?}}", "", text)
    return text

def tratarTexto(text):
    text = text.lower().strip()
    text = re.sub("[^a-z0-9çáéíóúàãõâêô-]", " ", text)
    return text

def getTextoAsDictionary():
    dicionario = {}
    tree = ET.parse('../ptwiki-v2.trec')
    root = tree.getroot()

    for docno, texto in zip(root.iter('DOCNO'), root.iter('P')):
        #dicionario[int(docno.text)] = tratar(texto.text)
        dicionario[int(docno.text)] = Counter(tratar(texto.text).split())
        #dicionario[headline.text] = tratar(texto.text)
    return dicionario



#print dicionario

