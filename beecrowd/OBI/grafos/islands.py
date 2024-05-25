import heapq
n, m = map(int, input().split())
# Inicializando a lista de adjacências
adj = [[] for _ in range(n)]

# Lendo as arestas e construindo o grafo
for _ in range(m):
    u, v, c = map(int, input().split())
    adj[u - 1].append((v - 1, c))
    adj[v - 1].append((u - 1, c))

s = int(input()) - 1

dist = [float("inf")] * n
mark = [False] * n

pq = []
heapq.heappush(pq,(0,s)  )
dist[s] = 0

while pq:
    weight,current = heapq.heappop(pq)

    if mark[current]: continue

    mark[current] = True 

    for j in range(len(adj[current])):
        neighbour = adj[current][j][0]
        w = adj[current][j][1]

        if dist[neighbour] > dist[current] + w:
            dist[neighbour] = dist[current] + w
            heapq.heappush(pq,(dist[neighbour],neighbour))

minimo = float("inf")
maximo = 0

for i in dist:
    if minimo > i and i != 0: 
        minimo = i
    if maximo < i:
        maximo = i

print(maximo-minimo)