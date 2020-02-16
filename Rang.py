from SetImpl import *
def odrediRang(set, rangStranice, imenaStranicaSaLinkovima):
    dictRang = {}
    for key1 in imenaStranicaSaLinkovima.keys():
        for value1 in imenaStranicaSaLinkovima[key1]:
            for key2, value2 in set._dict.items():
                if value1.replace("\\", "") == key2.replace("\\", ""):
                    if key2 not in dictRang.keys():
                        dictRang[value1] = value2

    print("Ispis rangova")
    for key, value in dictRang.items():
        print(key, value)

    rezultujuciSet = Set()

    for key, value in set._dict.items():
        rezultujuciSet.add(key, value)
    for key, value in rangStranice.items():
        rezultujuciSet.add(key, value)
    for key, value in dictRang.items():
        rezultujuciSet.add(key, value) 

    print("PRIKAZ KRAJNJEG SETA")
    for key, value in rezultujuciSet._dict.items():
        print(key, value)