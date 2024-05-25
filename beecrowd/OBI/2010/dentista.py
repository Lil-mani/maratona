k = qtd = 0
l = []
n = int(input())

for i in range(0, n):
    x, y = [int(x) for x in input().split()]
    l += [[y, x]]

l = sorted(l)
print(l)
for i in range(0, n):
    if l[i][1] >= k:
        qtd += 1
        k = l[i][0]

print(qtd)