n,c = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

voluntarios = 0
i = 0
j = len(arr)-1
while i < j:
    if arr[i] + arr[j] <= c:
        j-=1
        i+=1
        voluntarios+= 1
    else:
        voluntarios+=1
        j -= 1
if i == j:
    voluntarios+=1
print(voluntarios)