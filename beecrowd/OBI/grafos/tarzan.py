import sys
sys.setrecursionlimit(1000000000)

n,d = map(int,input().split())
visitados = [False]* n
adj = [[] for x in range(n)] # lista de adjacencia do grafo 
v = [] # vetor para coletar os pontos 
cnt = 0 

def distancia(p1,p2):
    return ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)

def dfs(current):
    if visitados[current]:
        return
    visitados[current] = True
    global cnt
    cnt+=1
    for v in adj[current]:
        dfs(v)

for i in range(n):
    x,y = map(int,input().split())
    v.append((x,y))

for i in range(n):
    for j in range(i+1,n):
        if distancia(v[i],v[j]) <= d*d:
            adj[i].append(j)
            adj[j].append(i)
dfs(0)
if n == cnt:
    print("S")
else:
    print("N")
    




