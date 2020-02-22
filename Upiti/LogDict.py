def unija(dict1,dict2):
    """ radi uniju nad 2 recnika"""
    dictVracanje={} #dict koji se vraca
    for (key1, value1) in dict1.items():
        dictVracanje[key1]=value1 #ovde dodajem sve u direktorijum
    for (key2, value2) in dict2.items():
        if key2 not in dict1.keys(): #proverava da li je kljuc iz drugog dict-a u prvom dict-u
            dictVracanje[key2] = value2 #ovde dodajem samo one koji nisu vec u direktorijumu 1
        else:
            dictVracanje[key2] += value2 #ako se key2 vec nalazi u dictVracanje onda mu samo uvecaj value
    return dictVracanje #vracam dictVracanje

def presek(dict1,dict2):
    """ radi presek nad 2 recnika"""
    dictVracanje = {} #dict koji se vraca
    for (key1, value1) in dict1.items():
        if key1 in dict2.keys(): #provera da li je kljuc iz prvog dict-a i u drugom dict-u
            #ovde dodajem samo one koji su u direktorijumu2 i u direkorijumu1
            pom = dict2[key1] #pomocna promenjiva koja cuva vrednost za kljuc iz dict2
            dictVracanje[key1] = value1 #ovde dodajem key1 i njegovu vrednost(iz prvog dicta) u dictVracanje
            dictVracanje[key1] += pom #ovde uvecavam vrednost za key1 u dictVracanje za pomocnu promenjivu(vrednost iz dict2)
    return dictVracanje #vracam dictVracanje

def komplement(dict1,dict2):
    """ radi komplement 2 recnika"""
    dictVracanje = {} #dict koji se vraca
    for (key1, value1) in dict1.items():
        if key1 not in dict2.keys():
            #ovde dodajem samo one koji su u direktorijumu1 a ne u direktorijumu2
            dictVracanje[key1] = value1 #dodajem key1 i njegovu vrednost ako je prosao kriterijum
    return dictVracanje #vracam dictVracanje