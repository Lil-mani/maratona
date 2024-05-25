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
G = int(input())
counter = 1
for _ in range(G):
    n = int(input())
    k = int(input())

    w = []
    v = []

    for i in range(n):
        val,wei = map(int,input().split())
        w.append(wei)
        v.append(val)

    res = knap(w,v,n,k)

    print("Galho {}:\nNumero total de enfeites: {}".format(counter,res))
    print()
    counter+=1