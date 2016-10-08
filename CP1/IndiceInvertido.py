#coding: utf-8
from Arquivo import getTextoAsDictionary
from time import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')



def booleanOR(array_palavras, indice_invertido):
    saida = []
    for palavra in array_palavras:
        try:
            saida = indice_invertido[u''.join(palavra.lower().decode())] + saida
        except KeyError:
            return "Nenhum documento contem a palavra: " + palavra
    return list(set(saida))

#Faz um "and" para apenas dois elementos
def AndDoisElementos(array_palavras, indice_invertido):
    saida = []
    ponteiro1 = 0
    ponteiro2 = 0
    try:
        posting1 = indice_invertido[u''.join(array_palavras[0].lower().decode())]
        posting2 = indice_invertido[u''.join(array_palavras[1].lower().decode())]
    except KeyError:
        return "Palavra nao encontrada."
    while ponteiro1 != len(posting1) and ponteiro2 != len(posting2):
        if posting1[ponteiro1] == posting2[ponteiro2]:
            saida.append(posting1[ponteiro1])
            ponteiro1 += 1
            ponteiro2 += 1
        elif posting1[ponteiro1] < posting2[ponteiro2]:
            ponteiro1 += 1
        else:
            ponteiro2 += 1
    return saida

#Faz and independente do numero de elementos
def AND(array_palavras, indice_invertido):
    postings = []
    saida = []
    ponteiros = []
    trava = True
    for palavra in array_palavras:
        try:
            postings.append(indice_invertido[u''.join(palavra.lower().decode())])
        except KeyError:
            return "Nenhum documento contem a palavra: " + palavra

        ponteiros.append(0)#inicia cada ponteiro com zero

    while trava:
        v = []
        ponteiros_incrementa = []
        for i in range(0, len(postings)):
            v.append(postings[i][ponteiros[i]])
        max_value = max(v)

        for i in range(0, len(v)):
            if v[i] != max_value:
                ponteiros_incrementa.append(i)
        if not ponteiros_incrementa:
            saida.append(max_value)
            for i in range(len(postings) - 1, -1, -1):
                ponteiros[i] += 1
                if len(postings[i]) == ponteiros[i]:
                    trava = False
                    break
        else:
            for i in ponteiros_incrementa:
                ponteiros[i] += 1
                if len(postings[i]) == ponteiros[i]: #ponteiro passou do array
                    trava = False
                    break

    return saida



comeco = time()
textos = getTextoAsDictionary()
print "Leitura de textos feita ..."
print time() - comeco
bagWords = []
dicionario = {}
for key in textos:
    for palavra in textos[key].split():
        if palavra not in bagWords:
            bagWords.append(palavra)
            if palavra in dicionario:
                dicionario[palavra].append(key)
            else:
                dicionario[palavra] = [key]
    bagWords = []

print "Indice Invertido criado ..."
print time() - comeco

print "nomes, biblícos"
#print AndDoisElementos(["nomes", "é"], dicionario)
print AND(["nomes", "bíblicos"], dicionario)
print booleanOR(["nomes", "bíblicos"], dicionario)
print "-=-=-=-=-=-"

print "Estados, Unidos"
print AND(["Estados", "Unidos"], dicionario)
print booleanOR(["Estados", "Unidos"], dicionario)
print "-=-=-=-=-=-"

print "Winston, Churchill"
print AND(["Winston", "Churchill"], dicionario)
print booleanOR(["Winston", "Churchill"], dicionario)


