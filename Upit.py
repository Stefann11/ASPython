import re
def provera(rec):
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