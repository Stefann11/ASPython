import re
def provera(rec):
    '''
    r = re.compile('[A-Za-z0-9]+')
    upitAnd = re.compile('[A-Za-z0+9]+ AND [A-Za-z0+9]+')
    upitOr = re.compile('[A-Za-z0+9]+ OR [A-Za-z0+9]+')
    upitNot = re.compile('[A-Za-z0+9]+ NOT [A-Za-z0+9]+')
    upitNotSam = re.compile('NOT [A-Za-z0+9]+')

    if upitAnd.match(rec):
        return 1
    elif upitOr.match(rec):
        return 2
    elif upitNotSam.match(rec):
        return 3
    elif upitNot.match(rec):
        return 4
    elif r.match(rec):
        return 5
    '''

    listaReci = []
    listaReci=rec.split(" ")
    counter = 0

    for i in listaReci:
        if i == "OR" or i == "AND" or i == "NOT" or i == "or" or i == "and" or i == "not":
            counter += 1

    if counter > 1:
        return 6, listaReci
    elif counter == 1:
        if listaReci[0] == "OR" or listaReci[0] == "AND" or listaReci[0] == "or" or listaReci[0] == "and" or listaReci[0] == "NOT" or listaReci[0] == "not":
            return 6, listaReci
        elif len(listaReci) == 3:
            if listaReci[1] == "AND" or listaReci[1] == "and":
                return 1, listaReci
            elif listaReci[1] == "OR" or listaReci[1] == "or":
                return 2, listaReci
            elif listaReci[1] == "NOT" or listaReci[1] == "not":
                return 4, listaReci
            else:
                return 6, listaReci
        else:
            return 6, listaReci
    else:
        return 5, listaReci
