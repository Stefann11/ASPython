from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
from Upit import *
from Set import *
from SetImpl import *
import os

def dodaj(inp):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp

    brojac = 0
    root = TrieNode('*')

    folder = os.fsencode(path)

    filenames = []


    parser = Parser()

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filename = os.fsdecode(file)
            if filename.endswith('.html'):

                finalPath = (os.path.join(subdir, file))
                # print(finalPath)
                filenames.append(filename)
                brojac = brojac + 1
                parser.parse(finalPath)
                for word in parser.words:
                    add(root, word.lower(), finalPath,parser.links,filename)

    print("Ukupan broj HTML stranica: ", brojac)
    return root


def trazi(root, rec):
    rec = rec.lower()

    dictStranica = {}
    dictLinkova = {}
    listaStranica = []
    set = Set()

    resenje = find_prefix(root,rec)
    dictStranica = resenje[2]
    print(dictStranica)
    dictLinkova = resenje[3]
    print(dictLinkova)
    print("Ukupan broj reci: ", resenje[1])
    listaStranica = resenje[4]
    set = resenje[5]




    return set, dictLinkova, listaStranica


if __name__ == "__main__":

    dictLinks = {}
    nameList = []
    resultSet = Set()

    set1 = Set()
    dictLinks1 = {}
    nameList1 = []

    set2 = Set()
    dictLinks2 = {}
    nameList2 = []


    listaReci = []

    print("Unesite korenski direktorijum")
    inp = input()

    print("Unesi rec koju zelis")
    rec = input()

    root=dodaj(inp)

    if root is None:
        print("Niste dobro uneli ulazni file")

    print(provera(rec))

    res=provera(rec)

    proveravaj=res[0]
    listaReci=res[1]

    if proveravaj == 1:
        print("AND upit")
        vraceno1 = trazi(root, listaReci[0])
        set1 = vraceno1[0]
        dictLinks1 = vraceno1[1]
        nameList1 = vraceno1[2]

        vraceno2 = trazi(root, listaReci[2])
        set2 = vraceno2[0]
        dictLinks2 = vraceno2[1]
        nameList2 = vraceno2[2]

        resultSet = set1.__and__(set2)

        for key, value in resultSet._dict.items():
            print(key, value)

        #dictLinks = presek(dictLinks1,dictLinks2)
        #print(dictLinks)
    elif proveravaj == 2:
        print("OR upit")
        vraceno1 = trazi(root, listaReci[0])
        set1 = vraceno1[0]
        dictLinks1 = vraceno1[1]
        nameList1 = vraceno1[2]

        vraceno2 = trazi(root, listaReci[2])
        set2 = vraceno2[0]
        dictLinks2 = vraceno2[1]
        nameList2 = vraceno2[2]

        resultSet=set1.__or__(set2)

        for key, value in resultSet._dict.items():
            print(key, value)

        #dictLinks = unija(dictLinks1, dictLinks2)
        #print(dictLinks)
    elif proveravaj == 3:
        print("NOT SAM upit")
        #listaReci=rec[4:]
        print(listaReci)
    elif proveravaj == 4:
        print("NOT upit")
        vraceno1 = trazi(root, listaReci[0])
        set1 = vraceno1[0]
        dictLinks1 = vraceno1[1]
        nameList1 = vraceno1[2]

        vraceno2 = trazi(root, listaReci[2])
        set2 = vraceno2[0]
        dictLinks2 = vraceno2[1]
        nameList2 = vraceno2[2]

        resultSet = set1.__not__(set2)
        for key, value in resultSet._dict.items():
            print(key, value)

        #dictLinks = komplement(dictLinks1, dictLinks2)
        #print(dictLinks)
    elif proveravaj==5:
        #listaReci=rec.split(" ")
        print(listaReci)

        for rec2 in listaReci:
            vraceno = trazi(root, rec2)
            set1 = vraceno[0]
            dictLinks1 = vraceno[1]
            nameList1 = vraceno[2]

            resultSet = resultSet.__or__(set1)
            #dictLinks=unija(dictLinks, dictLinks1)
        #print(dictLinks)
        for key, value in resultSet._dict.items():
            print(key, value)

    else:
        print("Nije dobar format")