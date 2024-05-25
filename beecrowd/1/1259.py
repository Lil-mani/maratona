n = int(input())
par = []
impar = []
for _ in range(n):
    values = int(input())
    if values%2 == 0:
        par.append(values)
    else:
        impar.append(values)

par.sort()
impar.sort(reverse=True)
i = 0
for i in par:
    print(i)

for i in impar:
    print(i)

