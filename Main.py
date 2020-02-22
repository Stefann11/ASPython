from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
from Upit import *
from LogDict import *
from SetImpl import *
from Iterator import *
from Paginacija import *
import os

if __name__ == "__main__":


    inp = 1
    direkt = 0
    izlaz = 1

    while direkt == 0 or inp != "0":
        print("Unesite korenski direktorijum, 0 za kraj")
        inp = input()

        if inp == "0":
            break

        prvaFunk = dodaj(inp)
        root = prvaFunk[0]
        if is_empty(root):
            print("Niste dobro uneli korenski direktorijum")
            direkt = 0
        else:
            direkt = 1

            while izlaz != "0":

                rec = 1
                print("Unesite 1 za ponovni unos direktorijuma")
                print("Unesite 2 za unos upita")
                print("Unesite 0 ukoliko želite da izadjete iz programa")
                izlaz = input()

                if izlaz == "0":
                    break

                if izlaz == "1":
                    direkt2 = 0
                    while direkt2 == 0:
                        print("Unesite korenski direktorijum")
                        inp = input()

                        prvaFunk = dodaj(inp)
                        root = prvaFunk[0]
                        if is_empty(root):
                            print("Niste dobro uneli korenski direktorijum")
                            direkt2 = 0
                        else:
                            direkt2 = 1
                elif izlaz == "2":
                    dictStranica = {}
                    dictLinks = {}
                    resultSet = Set()

                    set1 = Set()
                    dictLinks1 = {}
                    dictStranica1 = {}

                    set2 = Set()
                    dictLinks2 = {}
                    dictStranica2 = {}

                    rangStranica = {}
                    imenaStranicaSaLinkovima = {}

                    listaReci = []

                    print("Unesi upit koju želiš")
                    rec = input()

                    if rec == "0":
                        break


                    rangStranica = prvaFunk[1]
                    imenaStranicaSaLinkovima = prvaFunk[2]

                    res = provera(rec)

                    proveravaj=res[0]       # U zavisnosti od unosa upita i logickog operatora vraca broj koji predstavlja uneseni upit
                    listaReci=res[1]        # Lista reci u upitu
                    flag = 1                # Da li treba da se odredjuje rang

                    if rec == "":
                        print("Ne mozete uneti prazan string")
                    else:

                        if proveravaj == 1:         #za AND upit
                            vraceno1 = trazi(root, listaReci[0])    #za prvu rec (pre AND-a)
                            set1 = vraceno1[0]
                            dictLinks1 = vraceno1[1]
                            dictStranica1 = vraceno1[2]

                            vraceno2 = trazi(root, listaReci[2])     #za drugu rec (posle AND-a)
                            set2 = vraceno2[0]
                            dictLinks2 = vraceno2[1]
                            dictStranica2 = vraceno2[2]

                            resultSet = set1.__and__(set2)
                            dictStranica = presek(dictStranica1, dictStranica2)

                            if dictStranica == {}:
                                print("Ne postoje HTML stranice koje zadovoljavaju upit")

                            for item in resultSet._dict:
                                print(item)

                            for key,value in dictStranica.items():
                                print(key, value)

                        elif proveravaj == 2:           #za OR upit
                            vraceno1 = trazi(root, listaReci[0])     #za prvu rec (pre OR-a)
                            set1 = vraceno1[0]
                            dictLinks1 = vraceno1[1]
                            dictStranica1 = vraceno1[2]

                            vraceno2 = trazi(root, listaReci[2])    #za drugu rec (posle OR-a)
                            set2 = vraceno2[0]
                            dictLinks2 = vraceno2[1]
                            dictStranica2 = vraceno2[2]

                            resultSet=set1.__or__(set2)
                            dictStranica = unija(dictStranica1, dictStranica2)

                            if dictStranica == {}:
                                print("Ne postoje HTML stranice koje zadovoljavaju upit")

                            for item in resultSet._dict:
                                print(item)

                        elif proveravaj == 4:       #za NOT upit
                            vraceno1 = trazi(root, listaReci[0])
                            vraceno2 = trazi(root, listaReci[2])

                            set1 = vraceno1[0]      #za prvu rec (pre NOT-a)
                            dictLinks1 = vraceno1[1]
                            dictStranica1 = vraceno1[2]


                            set2 = vraceno2[0]      #za drugu rec (posle NOT-a)
                            dictLinks2 = vraceno2[1]
                            dictStranica2 = vraceno2[2]

                            resultSet = set1.__not__(set2)
                            dictStranica = komplement(dictStranica1, dictStranica2)

                            if dictStranica == {}:
                                print("Ne postoje HTML stranice koje zadovoljavaju upit")
                            for item in resultSet._dict:
                                print(item)

                        elif proveravaj==5:

                            for rec2 in listaReci:         #ukoliko ne postoji logicki operator
                                vraceno = trazi(root, rec2)

                                set1 = vraceno[0]
                                dictLinks1 = vraceno[1]
                                dictStranica1 = vraceno[2]

                                resultSet = resultSet.__or__(set1)
                                dictStranica = unija(dictStranica, dictStranica1)   #za svaki recnik povezi sa rezultujucim recnikom preko UNIJE
                            if dictStranica == {}:
                                print("Ne postoje HTML stranice koje zadovoljavaju upit")
                            for item in resultSet._dict:
                                print(item)

                        else:
                            print("Nije dobar format")
                            flag = 0

                        if flag == 1:
                            sortiraniDict = odrediRang(dictStranica, rangStranica, imenaStranicaSaLinkovima)
                            paginacija(sortiraniDict)
                elif izlaz == "0":
                    break
                else:
                    print("Morate da unesete jednu od ponudjenih opcija")