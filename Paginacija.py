import math

def paginacija(dict):
    n = 5
    while n != "0":
        print("Unesi broj stranica koji želiš da se prikaže, 0 ako želite da završite sa prikazivanjem")
        n = input()
        if n == "0":
            break

        n = int(n)

        m = len(dict) / n
        m = math.ceil(m)
        i = 0
        r = 2

        while r != 0:
            for j in range(i*n, (i+1)*n):
                if j < len(dict):
                    print(list(dict)[j], list(dict.values())[j])

            print("Unesite 1 za nazad, 3 ako želite da idete unapred ", n, " stranica, 0 ukoliko zelite da promenite broj stranica koje se prikazuju")
            r = input()
            if r == "1":
                i = i-1
            elif r == "3":
                i = i+1
            elif r == "0":
                break
            else:
                print("Pogresan unos")
            if i < 0:
                print("Vec ste na prvoj strani, ne mozete da idete u nazad")
                i = 0
            elif i + 1 > m:
                print("Vec ste na posledjoj strani, ne mozete da idete unapred")
                i = m-1




if __name__ == "__main__":
    c = 6/3
    c = math.ceil(c)
    print(c)

    dict = {'A' : 3, 'B' : 14, 'C' : 15, 'D' : 11, 'F' : 25, 'G' : 35, 'H' : 15, 'I' : 15, 'J' : 15}
    paginacija(dict)