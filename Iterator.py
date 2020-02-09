from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
from Upit import *
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

    resenje= find_prefix(root,rec)
    dictStranica=resenje[2]
    print(dictStranica)
    dictLinkova=resenje[3]
    print(dictLinkova)
    print("Ukupan broj reci: ", resenje[1])
    listaStranica=resenje[4]




    return dictStranica, dictLinkova, listaStranica


if __name__ == "__main__":

    dictionary = {}
    dictLinks = {}
    nameList = []
    listaReci = []

    print("Unesite korenski direktorijum")
    inp = input()

    print("Unesi rec koju zelis")
    rec = input()

    root=dodaj(inp)

    print(provera(rec))

    if provera(rec) == 1:
        print("AND upit")
        listaReci=rec.split(" AND ")
        print(listaReci)
    elif provera(rec) == 2:
        print("OR upit")
        listaReci=rec.split(" OR ")
        print(listaReci)
    elif provera(rec) == 3:
        print("NOT SAM upit")
        listaReci=rec[4:]
        print(listaReci)
    elif provera(rec) == 4:
        print("NOT upit")
        listaReci=rec.split(" NOT ")
        print(listaReci)
    elif provera(rec)==5:
        listaReci=rec.split(" ")
        print(listaReci)

        for rec2 in listaReci:
            vraceno = trazi(root, rec2)
            dictionary = vraceno[0]
            dictLinks = vraceno[1]
            nameList = vraceno[2]

            dodavanje(dictLinks, inp, nameList)
    else:
        print("Nije dobar format")



