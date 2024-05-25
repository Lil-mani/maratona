import math
t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    res = n/m
    print(math.ceil(res))