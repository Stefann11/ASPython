def provera(rec):

    listaReci = []
    listaReci=rec.split(" ")
    counter = 0

    for rec in listaReci:
        if rec == "":
            return 6, listaReci

    for i in listaReci:
        if i == "OR" or i == "AND" or i == "NOT" or i == "or" or i == "and" or i == "not":
            counter += 1

    if counter > 1:
        return 6, listaReci             # Ukoliko je broj operatora veci od 1, vrati 6 koje predstavlja gresku
    elif counter == 1:
        if listaReci[0] == "OR" or listaReci[0] == "AND" or listaReci[0] == "or" or listaReci[0] == "and" or listaReci[0] == "NOT" or listaReci[0] == "not":
            return 6, listaReci         # Ukoliko se na prvom mestu nalazi neki od log operatora vrati 6, greska
        elif len(listaReci) == 3:
            if listaReci[1] == "AND" or listaReci[1] == "and":
                return 1, listaReci     # Vrati 1 za and upit
            elif listaReci[1] == "OR" or listaReci[1] == "or":
                return 2, listaReci     # Vrati 2 za or upit
            elif listaReci[1] == "NOT" or listaReci[1] == "not":
                return 4, listaReci     # Vrati 4 za not upit
            else:
                return 6, listaReci     # Ukoliko postoji logicki operator, ali se ne nalazi na 2 mestu, vrati gresku
        else:
            return 6, listaReci         # Ukoliko postoji 1 logicki operator, ali broj reci nije jednak 3 vrati gresku
    else:
        return 5, listaReci             # Vrati 5, ukoliko ne postoji logicki operator
