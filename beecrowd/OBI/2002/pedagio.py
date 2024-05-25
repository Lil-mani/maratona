from queue import SimpleQueue
res = []
testecounter = 0
while True:
    try:
        c,e,l,p = map(int,input().split())
        if c == 0 and e == 0 and l == 0 and p == 0:
            break
        grafo = [[] for i in range(c)]
        for i in range(e):
            u,v = map(int,input().split())
            grafo[u-1].append(v-1)
            grafo[v-1].append(u-1)

        layer = [0] * c
        visitados = [False] * c

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
        bfs(l-1)
        guarda = []
        for i in range(c):
            if layer[i]<=p and i!= (l-1) and layer[i]!=0:
                guarda.append(i+1)
        testecounter+=1
        res.append(guarda)
    except EOFError:
        break

for i in range(testecounter):
    print("Teste", i+1)
    for element in res[i]:
        print(element,end=" ")
    print("\n")