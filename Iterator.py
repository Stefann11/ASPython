from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
from Upit import *
from LogDict import *
from SetImpl import *
from Rang import *
import os

def dodaj(inp):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp

    brojac = 0
    root = TrieNode('*')
    graf = Graph()
    set = Set()
    folder = os.fsencode(path)

    filenames = []
    dictGraf = {}
    rangStranica = {}
    imenaStranicaSaLinkovima = {}

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
                dictGraf[finalPath] = parser.links
                set.add(finalPath)
                for word in parser.words:
                    add(root, word.lower(), finalPath,parser.links,filename)

    rangStranica, imenaStranicaSaLinkovima = dodavanjeUGraf(graf,dictGraf,filenames)
    #print("Svi html fileovi sa svim linkovima")
    #print(dictGraf)
    print("Ukupan broj HTML stranica: ", brojac)
    return root, rangStranica, imenaStranicaSaLinkovima, set


def trazi(root, rec):
    rec = rec.lower()

    dictStranica = {}
    dictLinkova = {}
    listaStranica = []
    set = Set()

    resenje = find_prefix(root,rec)
    dictStranica = resenje[2]
    print(dictStranica)
    print("Linkovi na stranicama")
    dictLinkova = resenje[3]
    print(dictLinkova)
    print("Ukupan broj reci: ", resenje[1])
    listaStranica = resenje[4]
    set = resenje[5]




    return set, dictLinkova, listaStranica, dictStranica





