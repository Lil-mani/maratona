def bfs(begin, end):
    visited=[0]*(t+l+2)
    queue= []
    queue.append((begin,0))
    #for v in queue:
    while len(queue)>0:
        #print(v)
        v= queue.pop(0)
        for u in g[v[0]]:
            if(u==end):
                return v[1]
            if(not visited[u]):
                visited[u]=1
                if(u<=t):
                    queue.append((u,v[1]))
                else:
                    queue.append((u,v[1]+1))
                    
t,l,o,d= map(int,input().split())
g=[()]*(t+l+2)

for i in range(l):
    cities= list(map(int,input().split()))
    line_bus=i+1+t
    aux=[]
    for i in range(len(cities)):
        #print("out: ",line_idx,city)
        if(i==0):
            continue
        tp = list(g[cities[i]])
        tp.append(line_bus)
        g[cities[i]] = tuple(tp)
        aux.append(cities[i])
    g[line_bus]=tuple(aux)

print(g)
print(bfs(o,d))
    
