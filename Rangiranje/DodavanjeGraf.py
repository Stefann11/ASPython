def dodavanjeUGraf(graph, dict):
    rangStranica = {}
    imenaStranicaSaLinkovima = {}           #imena linkova sa stranicama
    for file in dict:                       #prolazi kroz sve html stranice u recniku
        graph.add_vertex(file)              #dodaje ih kao cvorove
        for link in dict[file]:             #prolazi kroz sve linkove u recniku
            graph.add_edge({file, link})    #dodaje ih kao grane
            if link in rangStranica:        #racuna koliko ce linkova pokazivati na neku html stranicu
                rangStranica[link]+=1       #plus 1 ako se link vec nalazi u rangStranica
            else:
                rangStranica[link] = 1      #dodaje link u rangStranica i postavlja mu rang na 1

            if link in imenaStranicaSaLinkovima:                    #pravi novi recnik gde je kljuc link a vrednost cvorovi koji sadrze taj link
                imenaStranicaSaLinkovima[link].append(file)         #u recniku za kljuc link dodajemo vrednost jos jednu html stranicu koja sadrzi taj link
            else:
                imenaStranicaSaLinkovima[link] = [file]             #u recniku za kljuc link postavljamo vrednost html stranicu koja sadrzi taj link


    return rangStranica, imenaStranicaSaLinkovima




