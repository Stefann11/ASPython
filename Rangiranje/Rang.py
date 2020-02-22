from Pagination_sort.Sort import *
def odrediRang(dictStranica, rangStranice, imenaStranicaSaLinkovima):
    dictRang = {}
    for key1 in imenaStranicaSaLinkovima.keys(): #idi po svim kljucevima tj. linkovima
        for value1 in imenaStranicaSaLinkovima[key1]: #idi po svim vrednostima tj. html stranicama koje sadrze trazeni link
            for key2, value2 in dictStranica.items(): #dictStranica za kljuceve ima html stranice a za vrednosti broj trazenih reci na njima
                if value1.replace("/", "").replace("\\", "") == key2.replace("/", "").replace("\\", ""): #resava problem kod poredjenja, koji se javljao usled pojvaljivanja '/' i '\' karaktera
                    if key2 not in dictRang.keys():
                        dictRang[value1] = value2 #dodaj u dictRang html stranicu kao kljuc i broj pojavljivanja trazene reci kao vrednost

    rezultujuciDict = {}

  #  print("ZA RECI ")
    for key, value in dictStranica.items(): #dictStranica za kljuceve ima html stranice a za vrednosti broj trazenih reci na njima
        #print(key, value) #za reci
        if key not in rezultujuciDict.keys():
            rezultujuciDict[key]=value  #dodaj u rezultujuciDict kljuc i vrednost iz dictStranica
        else:
            rezultujuciDict[key]+=value #ako vec postoji taj kljuc u rezultujuciDict samo mu saberi vrednost



    #print("ZA LINKOVE")
    for key, value in rangStranice.items(): #rangStranice sadrzi linkove za kljuceve i broj njihovih pojavljivanja kao linkova kao vrednost
        #print(key, value)#za linkove
        for key2, value2 in dictStranica.items():  #dictStranica za kljuceve ima html stranice a za vrednosti broj trazenih reci na njima
            if key2.replace("/", "\\") == key.replace("/", "\\"): #algoritam za proveravanje da li se neki link pojavljuje i kao cvor
                if key2 not in rezultujuciDict.keys():
                    rezultujuciDict[key2] = 2*value #ako se ne nalazi u rezultujuciDict dodaj ga (ovaj slucaj vrednujemo vise u ukupnom rangu, pa ga mnozimo sa 2)
                else:
                    rezultujuciDict[key2] += 2*value #ako se vec nalazi u rezulujuciDict, povecaj vrednost



    #print("ZA RECI U LINKOVIMA")
    for key, value in dictRang.items(): #dictRang kao kljuc sadrzi html stranice, a kao vrednost broj pojavljivanja trazene reci
        #print(key,value)#za reci u linkovima
        if key not in rezultujuciDict.keys():
            rezultujuciDict[key] = value #ako se ovaj kljuc ne nalazi u rezultujuciDict
        else:
            rezultujuciDict[key] += value #ako se ovaj kljuc nalazi u rezultujuciDict, dodaj value



    #print("Prikaz rangiranog rezultata") #nesortiran prikaz rezultata
    #for key, value in rezultujuciDict.items():
    #    print(key, value)

    rezultujuciDict = sortiranje(rezultujuciDict) #sortiraj rezultujuciDict

    if rezultujuciDict != {}: #provera da li nam je rezultujuciDict prazan
        print("Prikaz sortiranog rezultata") #sortiran prikaz rezultata
        for key, value in rezultujuciDict.items():
            print(key, value)
        return rezultujuciDict
