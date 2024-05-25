n = int(input())
p = list(map(int,input().split()))
p.sort()
c = 1 
for i in range(len(p)):
    if p[i] != c:
        break 
    c+=1

print(c)