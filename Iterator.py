from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
import os

def funkcija(inp, rec):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp
    rec=rec.lower()

    root = TrieNode('*')

    folder = os.fsencode(path)

    filenames = []
    brojac = 0
    dictStranica = {}
    dictLinkova = {}
    listaStranica = []

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

    resenje= find_prefix(root,rec)
    dictStranica=resenje[2]
    print(dictStranica)
    dictLinkova=resenje[3]
    print(dictLinkova)
    print(resenje[1])
    listaStranica=resenje[4]

    print(brojac)


    return dictStranica, dictLinkova, listaStranica


if __name__ == "__main__":

    dictionary = {}
    dictLinks = {}
    nameList = []

    print("Unesite korenski direktorijum")
    inp = input()

    print("Unesi rec koju zelis")
    rec = input()


    vraceno = funkcija(inp, rec)
    dictionary = vraceno[0]
    dictLinks = vraceno[1]
    nameList = vraceno[2]

    print("----------------------------------------")
    print(nameList)

    dodavanje(dictLinks, inp)


