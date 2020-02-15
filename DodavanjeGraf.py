from Graf2 import *
from Trie import *
import os

def dodavanjeUGraf(graph, dict, imeStranica):
    rangStranica = {}
    imenaStranicaSaLinkovima = {}
    odgovarajuciDict = {}
    for file in dict:
        graph.add_vertex(file)
        for link in dict[file]:
            # print(os.path.basename(link))
            # print(os.path.basename(file))
            if os.path.basename(link) in imeStranica:
                graph.add_edge({file, link})
                if link in rangStranica:
                    rangStranica[link]+=1
                else:
                    rangStranica[link] = 1

                if link in imenaStranicaSaLinkovima:
                    imenaStranicaSaLinkovima[link].append(file)
                else:
                    imenaStranicaSaLinkovima[link] = [file]

    '''
    print("Rang stranica")
    for key, value in rangStranica.items():
        print(key, value)
    print("Obrnuto")
    for key, value in imenaStranicaSaLinkovima.items():
        print(key,value)
    '''
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    return rangStranica, imenaStranicaSaLinkovima



