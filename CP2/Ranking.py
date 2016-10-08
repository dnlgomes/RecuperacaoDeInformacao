#coding: utf-8
from Arquivo import getTextoAsDictionary
from math import log
import operator
from collections import Counter
import sys

reload(sys)
sys.setdefaultencoding('utf8')


textos = getTextoAsDictionary()
print "Leitura de textos feita ..."

dicionario = {}
for key in textos:
    for palavra in textos[key]:
        if palavra in dicionario:
            dicionario[palavra][key] = textos[key][palavra]
        else:
            dicionario[palavra] = {key: textos[key][palavra]}

numero_documentos = len(textos)
new_indice = {}
for key in dicionario:
    indice = u''.join(key.lower().decode())
    idf = log( (numero_documentos + 1.0) / len(dicionario[indice]) )
    new_indice[key] = [idf, dicionario[indice]]



def BM25_Okapi(entrada, k):
    query = Counter(entrada.split())
    documents_values = {}
    for word in query:
        word = u''.join(word.lower().decode())
        for doc in new_indice[word][1]:
            if doc not in documents_values:
                documents_values[doc] = (query[word] * new_indice[word][0] * ( ((k + 1) * new_indice[word][1][doc]) / (new_indice[word][1][doc] + k) ))
            else:
                documents_values[doc] += (query[word] * new_indice[word][0] * ( ((k + 1) * new_indice[word][1][doc]) / (new_indice[word][1][doc] + k) ))
    sorted_dic = sorted(documents_values.items(), key=operator.itemgetter(1), reverse=True)[:5]
    return sorted_dic

print BM25_Okapi("primeira guerra mundial", 10)
print BM25_Okapi("espaço e tempo", 10)
print BM25_Okapi("minha terra tem palmeiras onde canta o sabiá", 10)
print BM25_Okapi("grupo raça negra", 10)
