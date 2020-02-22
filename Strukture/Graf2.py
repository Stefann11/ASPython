class Graph(object):

    def __init__(self, graph_dict=None):
        """ inicijalizuje graf, ako nije dat dictionary ili je None, koristice prazan dictionary"""
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ vraca cvorove grafa """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ vraca grane grafa """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ ako cvor nije vec u self.__graph_dict, kljuc "vertex" sa praznom listom za value ce biti dodat u dictionary.
            U suprotnom nista nece biti uradjeno.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ grana je tipa tuple, izmedju cvorova moze biti vise grana.
        """
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)  #dodaje linkove na cvor kao grane
        else:
            self.__graph_dict[vertex1] = [vertex2]    #dodaje prvi link na cvor kao granu

    def __generate_edges(self):
        """ Metoda za generisanje grana u grafu. Grane su skupovi sa jednim ili dva cvora
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})  #povezuje dva cvora (cvor i link)
        return edges



