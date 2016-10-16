#!/usr/bin/python
# coding: utf8
import re
import xml.etree.ElementTree as ET





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
    text = re.sub(r'\s+', ' ', text).strip()# substituir espaços em branco consecutivos por um unico espaco
    return text

#retorna um dicionario, com chave igual ao numero do documento, e os valores iguais ao texto do documento (ja tratados pela funcao tratar acima)
def getTextoAsDictionary():
    dicionario = {}
    tree = ET.parse('../ptwiki-v2.trec')
    root = tree.getroot()

    for docno, texto in zip(root.iter('DOCNO'), root.iter('P')):
        dicionario[int(docno.text)] = tratar(texto.text)
    return dicionario


#print tratar(getTextoAsDictionary()[1])


