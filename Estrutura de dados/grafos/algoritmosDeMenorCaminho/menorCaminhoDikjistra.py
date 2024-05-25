# acha o menor caminho de todos os vertices desde uma origem 
import heapq
n,m,s = map(int,input().split())
# Vertice source 
s = s-1 
adj = [[] for x in range(n)]

for i in range (m):
    u,v,c = map(int,input().split())
    # is_undirected = False 
    adj[u-1].append([v-1,c])
    adj[v-1].append([u-1,c])
del v
del c 
del u
dist = [float("inf")] * n
mark = [False] * n
# Fila de prioridade 
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


print(dist)