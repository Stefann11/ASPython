def dodavanjeUGraf(graph, dict):
    rangStranica = {}
    imenaStranicaSaLinkovima = {} #imena linkova sa stranicama
    for file in dict:   #prolazi kroz sve html stranice u direktorijumu
        graph.add_vertex(file) #dodaje ih kao cvorove
        for link in dict[file]:  #prolazi kroz sve linkove u direktorijumu
            graph.add_edge({file, link})  #dodaje ih kao grane
            if link in rangStranica:  #racuna koliko ce linkova imati neka html stranica
                rangStranica[link]+=1  #plus 1 za rang ako se link vec nalazi u rangStranica
            else:
                rangStranica[link] = 1  #dodaje link u rangStranica i postavlja mu rang na 1

            if link in imenaStranicaSaLinkovima:  #pravi novi direktorijum gde je key link a value cvorovi koji sadrze taj link
                imenaStranicaSaLinkovima[link].append(file) #na key link dodajemo value jos jednu html stranicu
            else:
                imenaStranicaSaLinkovima[link] = [file] #na key link dodajemo value jednu html stranicu


    return rangStranica, imenaStranicaSaLinkovima




