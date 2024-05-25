import sys
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

counter = 0
while True:
    try:
        n,c = map(int,input().split())

        if n == 0 and c == 0:
            break 
        counter+=1
        pesos = []
        profit = []
        for _ in range(n):
            w,v = map(int,input().split())
            pesos.append(w)
            profit.append(v)
        
        res = knap(pesos,profit,n,c)

        print("Caso {}: {}".format(counter,res))

    except EOFError:
        break