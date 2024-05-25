import sys
sys.setrecursionlimit(1000000)
def knap(wt,val,n,w):
    prev = [0] * (w+1)

    for i in range(wt[0],w+1):
        prev[i] = val[0]
    
    for ind in range(1,n):
        for cap in range(w,-1,-1):
            notTaken = 0 + prev[cap]

            taken = - sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + prev[cap - wt[ind]]
            prev[cap] = max(notTaken, taken)
    
    return prev[w]
t = int(input())
for _ in range(t):
    n = int(input())
    weights = []
    values = []

    for i in range(n):
        v,w = map(int,input().split())
        weights.append(w)
        values.append(v)

    k =int(input())
    destruicao = int(input())

    res = knap(weights,values,n,k)
    if res >= destruicao:
        print("Missao completada com sucesso")
    else:
        print("Falha na missao")