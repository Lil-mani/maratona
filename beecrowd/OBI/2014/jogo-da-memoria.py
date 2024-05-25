def bfs(graph, source, target):
    queue = []
    visited = [False] * len(graph)

    queue.append(source)
    visited[source] = True
    layer = [0] * len(graph)

    while len(queue) > 0:
        current = queue.pop(0)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                layer[neighbor] = layer[current] + 1
                if neighbor == target:
                    return layer[neighbor]

    return -1  # Retorna -1 se não houver caminho entre os nós

n = int(input())
cartas = list(map(int,input().split()))
dic = {}

for i in range(n):
    if cartas[i] not in dic:
        dic[cartas[i]] = [i]
    else:
        dic[cartas[i]].append(i)

adj = [[] for x in range(n)]

for _ in range(n-1):
    u,v = map(int,input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)


distTot = 0
for pairs in dic.keys():

    source = dic[pairs][0]
    target = dic[pairs][1]
    distTot+= bfs(adj,source,target)

print(distTot)
