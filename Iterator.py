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
                    add(root, word.lower(), finalPath,parser.links)

    resenje= find_prefix(root,rec)
    dictStranica=resenje[2]
    print(dictStranica)
    dictLinkova=resenje[3]
    print(dictLinkova)
    print(resenje[1])

    print(brojac)


    return dictStranica


if __name__ == "__main__":

    dictionary = {}

    print("Unesite korenski direktorijum")
    inp = input()

    print("Unesi rec koju zelis")
    rec = input()


    dictionary = funkcija(inp, rec)

    dodavanje(dictionary)


