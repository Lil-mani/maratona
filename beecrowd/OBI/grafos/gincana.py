# OBI 2011 - contar o numero de componentes 
import sys
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
grafo = [[] for _ in range (n)]
for i in range(m):
    u,v = map(int,input().split())
    grafo[u-1].append(v-1)
    grafo[v-1].append(u-1)

visitados = [False]* n
countGroups = 0
def dfs(current):
    visitados[current] = True 
    for i in grafo[current]:
        if not visitados[i]:
            dfs(i)

for i in range(n):
    if not visitados[i]:
        countGroups+=1
        dfs(i)

print(countGroups)





