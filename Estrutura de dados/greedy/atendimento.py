n = int(input())
arr = []

for _ in range(n):
    u,v = map(int,input().split())
    arr.append([u,v])

arr.sort(key= lambda x: x[1])

k = 0
cont = 0
for i in range(n):
    if arr[i][0] > k:
        cont+=1
        k = arr[i][1]

print(cont)