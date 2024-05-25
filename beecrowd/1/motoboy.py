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
while True:
    try: 
        n = int(input())
        if n == 0:
            break 
        v = int(input())

        weights = []
        values = []

        for _ in range(n):
            t,p = map(int,input().split())
            weights.append(p)
            values.append(t)

        res = knap(weights,values,n,v)
        print(res,"min.")
    except EOFError:
        break 
