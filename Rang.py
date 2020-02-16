from SetImpl import *
def odrediRang(dictStranica, rangStranice, imenaStranicaSaLinkovima):
    dictRang = {}
    for key1 in imenaStranicaSaLinkovima.keys():
        for value1 in imenaStranicaSaLinkovima[key1]:
            for key2, value2 in dictStranica.items():
                if value1.replace("\\", "") == key2.replace("\\", ""):
                    if key2 not in dictRang.keys():
                        dictRang[value1] = value2
    '''
    print("Ispis rangova")
    for key, value in dictRang.items():
        print(key, value)

    rezultujuciDict = {}
    
    for key, value in dictStranica.items():
        rezultujuciDict.add(key, value)
    for key, value in rangStranice.items():
        rezultujuciDict.add(key, value)
    for key, value in dictRang.items():
        rezultujuciDict.add(key, value)
    

    print("PRIKAZ KRAJNJEG SETA")
    for key, value in rezultujuciSet._dict.items():
        print(key, value)
    '''