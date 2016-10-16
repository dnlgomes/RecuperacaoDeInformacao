#!/usr/bin/python
# coding: utf8
import re
import xml.etree.ElementTree as ET
from collections import Counter



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


def getTextoAsDictionary():
    dicionario = {}
    tree = ET.parse('../ptwiki-v2.trec')
    root = tree.getroot()

    for docno, texto in zip(root.iter('DOCNO'), root.iter('P')):
        dicionario[int(docno.text)] = Counter(tratar(texto.text).split())
    return dicionario



#print dicionario

