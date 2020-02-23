from Add_search_parser.parserReci import Parser
from Strukture.Trie import *
from Strukture.Graf2 import *
#from builtins import print
from Rangiranje.DodavanjeGraf import *
import os

def dodaj(inp):
    #path = 'C:/Users/Korisnik/PycharmProjects/ASPython/test-skup/python-2.7.7-docs-html'

    path = inp                  # Unesena vrednost path-a

    brojac = 0                  # Brojac za HTML stranice
    root = TrieNode('*')        # Napravi novi trie
    graf = Graph()              # Napravi novi graf
    folder = os.fsencode(path)

    filenames = []
    dictGraf = {}               # Recnik koji ce cuvati sve HTML stranice i linkove na njima, koji cemo dodavati u graf
    rangStranica = {}           # Recnik za odredjivanje ranga (cuva HTML stranice i broj linkova koji pokazuju ka njima)
    imenaStranicaSaLinkovima = {}   # Recnik za odredjivanje ranga (cuva HTML stranice i sve linkove koji pokazuju ka njoj)

    parser = Parser()


    for subdir, dirs, files in os.walk(path):                    # Prolazak kroz sve file-ove za zadati korenski direktorijum
        for file in files:
            filename = os.fsdecode(file)
            if filename.endswith('.html'):

                finalPath = (os.path.join(subdir, file))          # Putanja do HTML file-a
                filenames.append(filename)
                brojac = brojac + 1                               # Povecaj vrednost brojaca HTML stranica
                parser.parse(finalPath)                           # Parsiraj HTML stranicu (celu putanju)
                dictGraf[finalPath] = parser.links                # Popunjavaj recnik za graf
                for word in parser.words:
                    add(root, word.lower(), finalPath,parser.links)     # Svaku rec u parsiranoj stranici dodaj u Trie

    rangStranica, imenaStranicaSaLinkovima = dodavanjeUGraf(graf,dictGraf)      #Dodavanje u graf
    #print("Svi html fileovi sa svim linkovima")
    #print(dictGraf)
    print("Ukupan broj HTML stranica: ", brojac)
    return root, rangStranica, imenaStranicaSaLinkovima


def trazi(root, rec):
    rec = rec.lower()

    dictStranica = {}
    dictLinkova = {}
    set = Set()

    resenje = find_prefix(root,rec)                       # Pretrazivanje trie-a u zavisnosti od vrednosti parametra rec
    if resenje is not None:                               # Ukoliko smo uspesno pretrazili trie
        dictStranica = resenje[2]                         # Recnik sa HTML stranicama i brojem trazene reci na njima
        #print(dictStranica)
        #print("Linkovi na stranicama")
        dictLinkova = resenje[3]                          # Recnik sa HTML stranicama i linkovima na njima
        #print(dictLinkova)
        #print("Ukupan broj reci: ", resenje[1])
        set = resenje[4]                                  # Skup HTML stanica koje zadovoljavaju upit




        return set, dictLinkova, dictStranica

    return Set(), {}, {}                                    # Ukoliko nismo uspesno pronasli trazenu rec u trie



