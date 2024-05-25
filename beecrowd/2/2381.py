n,k = map(int,input().split())
arr = []
for i in range(n):
    arr.append(input())

arr.sort()
print(arr[k-1])