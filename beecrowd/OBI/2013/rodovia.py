import sys
sys.setrecursionlimit(1000000)

n = int(input())
grafo = [0] * (n+1)
for i in range(n):
    u,v = map(int,input().split())
    grafo[u] = v
aux = 1
for i in range(1,n+1):
    aux = grafo[aux]
    if i != n and aux == 1:
        aux = 2
        break

if aux == 1:
    print("S")
else:
    print("N")



