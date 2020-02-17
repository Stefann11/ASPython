from SetImpl import *
from Sort import *
def odrediRang(dictStranica, rangStranice, imenaStranicaSaLinkovima):
    dictRang = {}
    print("Odavde")
    for key1 in imenaStranicaSaLinkovima.keys():
        for value1 in imenaStranicaSaLinkovima[key1]:
            for key2, value2 in dictStranica.items():
                if value1.replace("\\", "") == key2.replace("\\", ""):
                    if key2 not in dictRang.keys():
                        dictRang[value1] = value2

    print("Ispis rangova")
    #for key, value in dictRang.items():
    #    print(key, value)

    rezultujuciDict = {}

    print("ZA RECI ")
    for key, value in dictStranica.items():
        print(key, value) #za reci
        if key not in rezultujuciDict.keys():
            rezultujuciDict[key]=value
        else:
            rezultujuciDict[key]+=value

    print("ZA LINKOVE")
    for key, value in rangStranice.items():
        print(key, value)#za linkove
        for key2, value2 in dictStranica.items():
            if key2.replace("/", "\\") == key.replace("/", "\\"):
                if key2 not in rezultujuciDict.keys():
                    rezultujuciDict[key2] = 2*value
                else:
                    rezultujuciDict[key2] += 2*value

    print("ZA RECI U LINKOVIMA")
    for key, value in dictRang.items():
        print(key,value)#za reci u linkovima
        if key not in rezultujuciDict.keys():
            rezultujuciDict[key] = value
        else:
            rezultujuciDict[key] += value



    print("Prikaz rangiranog rezultata")
    for key, value in rezultujuciDict.items():
        print(key, value)

    rezultujuciDict = sortiranje(rezultujuciDict)

    print("Prikaz sortiranog rezultata")
    for key, value in rezultujuciDict.items():
        print(key, value)
