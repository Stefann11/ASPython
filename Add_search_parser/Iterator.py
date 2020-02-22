from Add_search_parser.parserReci import Parser
from Strukture.Trie import *
from Strukture.Graf2 import *
from builtins import print
from Rangiranje.DodavanjeGraf import *
import os

def dodaj(inp):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp

    brojac = 0
    root = TrieNode('*')
    graf = Graph()
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
                filenames.append(filename)
                brojac = brojac + 1
                parser.parse(finalPath)
                dictGraf[finalPath] = parser.links
                for word in parser.words:
                    add(root, word.lower(), finalPath,parser.links)

    rangStranica, imenaStranicaSaLinkovima = dodavanjeUGraf(graf,dictGraf)
    #print("Svi html fileovi sa svim linkovima")
    #print(dictGraf)
    print("Ukupan broj HTML stranica: ", brojac)
    return root, rangStranica, imenaStranicaSaLinkovima


def trazi(root, rec):
    rec = rec.lower()

    dictStranica = {}
    dictLinkova = {}
    set = Set()

    resenje = find_prefix(root,rec)
    if resenje is not None:
        dictStranica = resenje[2]
        #print(dictStranica)
        #print("Linkovi na stranicama")
        dictLinkova = resenje[3]
        #print(dictLinkova)
        #print("Ukupan broj reci: ", resenje[1])
        set = resenje[4]




        return set, dictLinkova, dictStranica

    return Set(), {}, {}



