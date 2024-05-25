n = int(input())

v = input()
v = list(map(int, v.split()))
v.sort()
flag = 0
for i in range(2,len(v)):
    if v[i-1] + v[i-2] >v[i]:
        flag = 1
        break
if flag == 1:
    print("YES")
else:
    print("NO")