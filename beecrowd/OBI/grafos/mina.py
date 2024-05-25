# Dijkistra pra uma matriz 
# O problema pede para basicamente achar o menor custo em uma matriz 
# onde o 1 representa as pedras do problema é temos que escolher o caminho 
# com menor custo de pedras (quebrar a menor quantidade de pedras) 
import heapq
n = int(input())
mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))
# todos os valores da array de distancia seram inf 
# para ser possivel achar o menor caminho a partir de 00
dist = [[float("inf") for x in range(n)] for y in range(n)]
# visitados = [[False for x in range(n)] for y in range(n)]
dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

# visitados[0][0] = True 
dist[0][0] = 0
#  peso, coordenada x, coordenada y 
pq = [[dist[0][0],0,0]]
heapq.heapify(pq) 

while len(pq) > 0:
    custo,x,y = heapq.heappop(pq)

    # Garatindo que estamos explorando caminhos descobertos 
    if custo == dist[x][y]:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            # Out of range 
            if a<0 or b <0: continue
            if a>=n or b>=n: continue

            custo = mat[a][b]
            if dist[a][b] > custo + dist[x][y]:
                dist[a][b] = dist[x][y] + custo
                heapq.heappush(pq,[dist[a][b],a,b])

print(dist[n-1][n-1])





