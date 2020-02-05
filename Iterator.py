from parserReci import Parser
from Trie import *
from builtins import print
import os

def funkcija(inp):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp

    folder = os.fsencode(path)

    filenames = []
    brojac=0

    parser = Parser()
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filename = os.fsdecode(file)
            if filename.endswith( ('.html') ):
                finalPath=(os.path.join(subdir, file))
                #print(finalPath)
                filenames.append(filename)
                brojac=brojac+1
                parser.parse(finalPath)


    print(brojac)


    print(parser.words)


if __name__ == "__main__":

    root = TrieNode('*')
    print("Unesite korenski direktorijum")
    inp = input()
    funkcija(inp)



