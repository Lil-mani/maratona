n = int(input())
arr = list(map(int,input().split()))

p = 0
res = float('-inf')
for i in range(n):
    p+= arr[i]
    res = max(res,p)
    p = max(p,0)

print(res)
