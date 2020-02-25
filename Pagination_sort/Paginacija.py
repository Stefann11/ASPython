import math

def paginacija(dict):
    '''
    if dict is not None:
        n = 5

        while n != "0":     #radi sve dok ne unese 0 za n
            print("Unesite broj stranica koje želite da se prikažu. Broj pronađenih stranica: ",len(dict),". Stranice su sortirane po rangu. Unesite 0 ako želite da završite sa prikazivanjem")
            n = input()     #unos n
            if n == "0":    #izadji ako je n jednako 0
                break

            n = int(n)      #prebacivanje n u integer

            m = len(dict) / n   #racunam koliko ce stranica biti
            m = math.ceil(m)    #zaokruzejem taj broj na veci
            i = 0
            r = 2       #postavljam r na random broj, razlicit od 0

            while r != 0:       #ponavljaj dok je r razlicito od 0
                for j in range(i*n, (i+1)*n):   #algoritam za ispis n stranica, od prve do n-te, zatim od stranice n+1 do 2*n...
                    if j < len(dict):   #dok j nije izaslo iz opsega dict-a
                        print(list(dict)[j], list(dict.values())[j])    #ispisi html stranicu i rang

                print("Unesite 1 da bi išli jednu stranu unazad, 3 ako želite da idete unapred jednu stranu, 0 ukoliko zelite da promenite broj stranica koje se prikazuju")
                r = input()     #unesi r, koji nam govori sta dalje radimo
                if r == "1":
                    i = i-1     #vrati jednu stranu unazad
                elif r == "3":
                    i = i+1     #idi jednu stranu unapred
                elif r == "0":
                    break       #ako je nula, izadji
                else:
                    print("Pogresan unos")
                if i < 0:
                    print("Vec ste na prvoj strani, ne mozete da idete u nazad")
                    i = 0       #ogranicenje da je na prvoj strani, a i postavljamo na 0, kako bi ostali na prvoj strani
                elif i + 1 > m:
                    print("Vec ste na posledjoj strani, ne mozete da idete unapred")
                    i = m-1     #ogranicenje da je na poslednjoj strani, a i postavljamo na m-1, kako bi ostali na poslednjoj strani
    '''


    if dict is not None:  # proveravamo da li je dict razlciit od none
        n = 5  # pocetna vrednost broja stranica
        r = 1  # postavljamo n na neki random broj, razlicit od 0

        i = 0

        print("Broj pronadjenih stranica je: ", len(dict))

        while r != 0:  # ponavljaj dok je r razlicito od 0
            m = len(dict) / n  # racunam koliko ce stranica biti
            m = math.ceil(m)  # zaokruzejem taj broj na veci

            for j in range(i * n, (
                                          i + 1) * n):  # algoritam za ispis n stranica, od prve do n-te, zatim od stranice n+1 do 2*n...
                if j < len(dict):  # dok j nije izaslo iz opsega dict-a
                    print(list(dict)[j], list(dict.values())[j])  # ispisi html stranicu i rang

            print(
                "Unesite 1 da bi išli jednu stranu unazad, 3 ako želite da idete unapred jednu stranu, 4 ukoliko zelite da promenite broj stranica koje se prikazuju, 0 za kraj")
            r = input()  # unesi r, koji nam govori sta dalje radimo
            if r == "1":
                i = i - 1  # vrati jednu stranu unazad
            elif r == "3":
                i = i + 1  # idi jednu stranu unapred
            elif r == "4":
                n, i = menjajBroj(n, i)
            elif r == "0":
                break  # ako je nula, izadji
            else:
                print("Pogresan unos")
            if i < 0:
                print("Vec ste na prvoj strani, ne mozete da idete u nazad")
                i = 0  # ogranicenje da je na prvoj strani, a i postavljamo na 0, kako bi ostali na prvoj strani
            elif i + 1 > m:
                print("Vec ste na posledjoj strani, ne mozete da idete unapred")
                i = m - 1  # ogranicenje da je na poslednjoj strani, a i postavljamo na m-1, kako bi ostali na poslednjoj strani


def menjajBroj(broj, iter):
    print("Unesite broj stranica koje želite da se prikažu.")
    n = input()  # unos n
    if n == "0" or n == "":  # izadji ako je n jednako 0
        print("Nemoguć unos, broj će ostati isti")
        return broj, iter

    n = int(n)  # prebacivanje n u integer
    return n, 0



