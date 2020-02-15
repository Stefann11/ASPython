from parserReci import Parser
from Trie import *
from builtins import print
from DodavanjeGraf import *
from Upit import *
from Set import *
from SetImpl import *
from Iterator import *
import os

if __name__ == "__main__":

    rec = 1
    inp = 1

    dictLinks = {}
    nameList = []
    resultSet = Set()
    ceoSet = Set()

    set1 = Set()
    dictLinks1 = {}
    nameList1 = []

    set2 = Set()
    dictLinks2 = {}
    nameList2 = []

    rangStranica = {}
    imenaStranicaSaLinkovima = {}

    listaReci = []

    while inp != "0":
        print("Unesite korenski direktorijum, 0 za kraj")
        inp = input()

        if inp=="0":
            break

        prvaFunk = dodaj(inp)
        root = prvaFunk[0]
        if is_empty(root):
            print("Niste dobro uneli korenski direktorijum")
        else:
            while rec != "0":
                print("Unesi rec koju zelis, 0 za kraj")
                rec = input()

                if rec == "0":
                    break


                rangStranica = prvaFunk[1]
                imenaStranicaSaLinkovima = prvaFunk[2]
                ceoSet = prvaFunk[3]

                res=provera(rec)

                proveravaj=res[0]
                listaReci=res[1]

                flag = 1

                if rec == "":
                    print("Ne mozete uneti prazan string")
                else:

                    if proveravaj == 1:
                        print("AND upit")
                        vraceno1 = trazi(root, listaReci[0])
                        set1 = vraceno1[0]
                        dictLinks1 = vraceno1[1]
                        nameList1 = vraceno1[2]

                        vraceno2 = trazi(root, listaReci[2])
                        set2 = vraceno2[0]
                        dictLinks2 = vraceno2[1]
                        nameList2 = vraceno2[2]

                        resultSet = set1.__and__(set2)

                        for key, value in resultSet._dict.items():
                            print(key, value)

                        #dictLinks = presek(dictLinks1,dictLinks2)
                        #print(dictLinks)
                    elif proveravaj == 2:
                        print("OR upit")
                        vraceno1 = trazi(root, listaReci[0])
                        set1 = vraceno1[0]
                        dictLinks1 = vraceno1[1]
                        nameList1 = vraceno1[2]

                        vraceno2 = trazi(root, listaReci[2])
                        set2 = vraceno2[0]
                        dictLinks2 = vraceno2[1]
                        nameList2 = vraceno2[2]

                        resultSet=set1.__or__(set2)

                        for key, value in resultSet._dict.items():
                            print(key, value)

                        #dictLinks = unija(dictLinks1, dictLinks2)
                        #print(dictLinks)
                    elif proveravaj == 3:
                        print("NOT SAM upit")
                        vraceno = trazi(root, listaReci[1])
                        set2 = vraceno[0]
                        dictLinks2 = vraceno[1]
                        nameList2 = vraceno[2]

                        resultSet = ceoSet.__not__(set2)
                        for key, value in resultSet._dict.items():
                            print(key, value)
                    elif proveravaj == 4:
                        print("NOT upit")
                        vraceno1 = trazi(root, listaReci[0])
                        set1 = vraceno1[0]
                        dictLinks1 = vraceno1[1]
                        nameList1 = vraceno1[2]

                        vraceno2 = trazi(root, listaReci[2])
                        set2 = vraceno2[0]
                        dictLinks2 = vraceno2[1]
                        nameList2 = vraceno2[2]

                        resultSet = set1.__not__(set2)
                        for key, value in resultSet._dict.items():
                            print(key, value)

                        #dictLinks = komplement(dictLinks1, dictLinks2)
                        #print(dictLinks)
                    elif proveravaj==5:
                        #listaReci=rec.split(" ")
                        print(listaReci)

                        for rec2 in listaReci:
                            vraceno = trazi(root, rec2)
                            set1 = vraceno[0]
                            dictLinks1 = vraceno[1]
                            nameList1 = vraceno[2]

                            resultSet = resultSet.__or__(set1)
                            #dictLinks=unija(dictLinks, dictLinks1)
                        #print(dictLinks)
                        for key, value in resultSet._dict.items():
                            print(key, value)

                    else:
                        print("Nije dobar format")
                        flag = 0

                    if flag == 1:
                        odrediRang(resultSet, rangStranica, imenaStranicaSaLinkovima)