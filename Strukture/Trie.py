from Strukture.SetImpl import *


class TrieNode(object):


    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False      #Za poslednji znak u reci
        self.counter = 0                #Ukupan broj pojavljivanja
        self.listDict={}                #Recnik u koji ce biti smesteni HTML stranice i svi linkovi na njoj
        self.pathDict={}                #Recnik u koji ce biti smesteni HTML stranice i broj pojavljivanja trazene reci na tim stranicama
        self.pathSet = Set()            #Set za cuvanje HTML stranica

def is_empty(root):                     #Da li je prazno stablo (da li je smo poslali dobar pocetni direktorijum)
    node = root
    return node.children == []

def add(root, word: str, path, links):
    #Dodavanje reci u stablo

    node = root
    for char in word:
        found_in_child = False
        #Provera da li vec postoji to slovo u deci trenutnog cvora
        for child in node.children:
            if child.char == char:
                #Ukoliko smo ga pronasli
                node = child
                found_in_child = True

                break
        # Ako nismo treba napraviti novo dete za tim slovom
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    # Postaviti promenljivu za kraj reci na True
    node.word_finished = True
    if path in node.pathDict:       # Ukoliko postoji u recniku vec vrednost kljuca koja je poslata HTML stranica, vrednost povecati vrednost broja reci za jedan
        node.pathDict[path]+=1
    else:                           # Ukoliko ne postoji u recniku, postaviti vrednost na 1
        node.pathDict[path]=1
        node.listDict[path]=links   # Dodati sve linkove koji se nalaze na toj stranici(kljuc- HTML stranica, vrednost- svi linkovi na njoj)

    node.pathSet.add(path)          # Dodati HTML stranicu u skup(Set)

    node.counter += 1               # Povecati ukupan broj reci za 1


def find_prefix(root, prefix: str):
    """
    Proverava da li se rec nalazi u Trie, ukoliko se nalazi vratice ukupan broj pojavljivanje, recnike za broj reci i linkove na stranicama
    """
    node = root
    # Ukoliko postoji dece ne trebamo da pretrazujemo jer je prazan Trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Pretrazi za svu decu u trenutnom cvoru (node)
        for child in node.children:
            if child.char == char:
                # Ukoliko smo nasli, to zabelezimo u char_not_found
                char_not_found = False
                # Cvor postaviti vrednost deteta u kom smo nasli slovo
                node = child
                break
        # Ukoliko nismo nasli slovo
        if char_not_found:
            return False, 0, {}, {}, Set()
    # Ukoliko smo nasli slovo i predstavlja kraj reci
    if node.word_finished:
        return True, node.counter, node.pathDict, node.listDict, node.pathSet
