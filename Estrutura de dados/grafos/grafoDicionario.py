class WeightedGraph:
    def __init__(self,directed=False):
        self.graph = {}
        self.directed = directed
    
    def add_node(self,u,v,w):
        if u not in self.graph:
            self.graph[u] = [(v,w)]
        else:
            self.graph[u].append((v,w))
        
        # Se for um grafo direcional 
        if self.directed is True:
            if v in self.graph:
                self.graph[v].append((u,v))
            else:
                self.graph[v] = [(u,v)]
    
    def print_graph(self):
        for vertex in self.graph:
            print(vertex,' -> ',self.graph[vertex])
    



grafo = WeightedGraph()
grafo.add_node('A','B',5)
grafo.add_node('A','C',10)
grafo.add_node('B','C',3)
grafo.add_node('C','B',2)

grafo.print_graph()