def unija(dict1,dict2):
    dictVracanje={}
    i = 0
    for (key1, value1) in dict1.items():
        #ovde dodajem sve u direktorijum
        dictVracanje[key1]=value1
    for (key2, value2) in dict2.items():
        if key2 not in dict1.keys():
            #ovde dodajem samo one koji nisu vec u direktorijumu1
            dictVracanje[key2]=value2
    return dictVracanje

def presek(dict1,dict2):
    dictVracanje = {}
    i = 0
    for (key1, value1) in dict1.items():
        if key1 in dict2.keys():
            #ovde dodajem samo one koji su u direktorijumu2 i u direkorijumu1
            dictVracanje[key1]=value1
    return dictVracanje

def komplement(dict1,dict2):
    dictVracanje = {}
    i = 0
    for (key1, value1) in dict1.items():
        if key1 not in dict2.keys():
            #ovde dodajem samo one koji su u direktorijumu1 a ne u direktorijumu2
            dictVracanje[key1]=value1
    return dictVracanje