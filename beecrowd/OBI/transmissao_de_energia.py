
resultados = []
while True:
    try:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        grafo = [[] for x in range (n)]

        for i in range(m):
            u,v = map(int,input().split())
            grafo[u-1].append(v-1)
            grafo[v-1].append(u-1)
        
        visitados = [False] * n
        counter = 0
        def dfs(current):
            visitados[current] = True 
            for i in grafo[current]:
                if not visitados[i]:
                    dfs(i)
        
        for i in range(n):
            if not visitados[i]:
                counter+=1
                dfs(i)
        if counter > 1:
            resultados.append("falha")
        else:
            resultados.append("normal")
    except EOFError:
        break


for i,value in enumerate(resultados):
    print("Teste",i+1)
    print(value)
    print()