from parserReci import Parser
from Trie import *
from builtins import print
import os


def funkcija(inp, rec):
    # path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp
    rec = rec.lower()

    root = TrieNode('*')

    folder = os.fsencode(path)

    filenames = []
    brojac = 0
    brojacReci = []
    listaStranica = []
    dictStranica = {}
    x = 0

    parser = Parser()
    '''
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filename = os.fsdecode(file)
            if filename.endswith('.html'):

                finalPath = (os.path.join(subdir, file))
                #print(finalPath)
                filenames.append(filename)
                brojac = brojac+1
                parser.parse(finalPath)
                x = 0
                for word in parser.words:
                    add(root, word)
                    if word == rec:
                        x += 1
                        listaStranica.append(finalPath)

                brojacReci.append(x)

            pomocna=find_prefix(root, rec)


            #brojacReci.append(pomocna[1])

    listaStranica = list(dict.fromkeys(listaStranica))

    brojacReci[:] = (value for value in brojacReci if value != 0)

    j=0
    for i in listaStranica:
        print(i, brojacReci[j])
        j+=1
        '''

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filename = os.fsdecode(file)
            if filename.endswith('.html'):

                finalPath = (os.path.join(subdir, file))
                # print(finalPath)
                filenames.append(filename)
                brojac = brojac + 1
                parser.parse(finalPath)
                x = 0
                for word in parser.words:
                    word = word.lower()
                    add(root, word, finalPath)

    # print(find_prefix(root, rec))
    '''
    resenje=find_prefix(root, rec)
    listaStranica=resenje[2]
    listaStranica = list(dict.fromkeys(listaStranica))
    print(resenje[1], listaStranica)
    '''

    resenje = find_prefix(root, rec)
    dictStranica = resenje[2]
    print(dictStranica)

    print(brojac)
    print(brojacReci)


if __name__ == "__main__":
    print("Unesite korenski direktorijum")
    inp = input()

    print("Unesi rec koju zelis")
    rec = input()

    funkcija(inp, rec)
