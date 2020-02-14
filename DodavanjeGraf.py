from Graf2 import *
import os

def dodavanjeUGraf(graph, dict, imeStranica):
    for file in dict:
        graph.add_vertex(file)
        for link in dict[file]:
            # print(os.path.basename(link))
            # print(os.path.basename(file))
            if os.path.basename(link) in imeStranica:
                graph.add_edge({file, link})



    #print("Vertices of graph:")
    #print(graph.vertices())

    #print("Edges of graph:")
    #print(graph.edges())



