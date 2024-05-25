# O bfs pode ser utilizado para procurar caminhos mais curtos dado dois vertices A e B
# de um grafo sem pesos 
from queue import SimpleQueue
grafo = [[1], [0, 2], [1, 3], [2, 4], [3]]
A = 0
B = 6
n = len(grafo)
layer = [0]*n
visitados = [False] * n

def bfs(source):
    q = SimpleQueue()
    q.put(source)
    visitados[source] = True
    layer[source] = 0

    while not q.empty():
        current = q.get()

        for i in range(len(grafo[current])):
            neighbour = grafo[current][i]

            if visitados[neighbour]:
                continue
            q.put(neighbour)
            visitados[neighbour] = True
            layer[neighbour] = (layer[current]+1)
bfs(1)

# print(layer[B])
print(layer)



