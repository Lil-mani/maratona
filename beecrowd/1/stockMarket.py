n,c = map(int,input().split())
stocks = list(map(int,input().split()))

p = 0
res = float('-inf')

for i in range(n):
    p = p - stocks[i] - c
    res = max(res,p)
    p = min(p,stocks[i])