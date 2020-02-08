from Graf2 import *
import os

def dodavanje(dict, inp):
    graph = Graph()


    '''
    for file in dict:

    for link in dict.values():
        #print(link)
        '''
    poc = inp
    for file in dict:
        graph.add_vertex(file)
        for link in dict[file]:
            print(os.path.basename(link))
            if os.path.basename(link) in dict.keys():
                graph.add_edge(file, link)
            inp = poc


    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())



