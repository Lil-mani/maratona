t = int(input())
res = []
for _ in range(t):
    s = sorted(input().split(),key= lambda x: len(x),reverse=True)
    res.append(s)

for i in range(t):
    for j in res[i]:
        print(j,end=" ")
    print()