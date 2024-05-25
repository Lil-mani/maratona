from queue import SimpleQueue
n,a,b = map(int,input().split())
grafo = [[] *x for x in range(n)]
for i in range(n-1):
    u,v = map(int,input().split())
    grafo[u-1].append(v-1)
    grafo[v-1].append(u-1)

visitados = [False] * n
layer = [0] * n
def bfs(source):
    q = SimpleQueue()
    q.put(source)
    visitados[source] = True
    layer[source] = 0
    while not q.empty():
        current = q.get()
        for i in range (len(grafo[current])):
            neigh = grafo[current][i]
            if visitados[neigh]:
                continue
            visitados[neigh] = True 
            q.put(neigh)
            layer[neigh]+= (layer[current]+1)
bfs(a-1)
print(layer[b-1])