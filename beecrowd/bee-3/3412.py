n = int(input())
r = []
for _ in range(n):
    nome = input()
    notas = list(map(float,input().split()))
    if len(notas) <= 2:
        r.append('{}: {:.1f}'.format(nome,sum(notas)/2))
    elif len(notas) == 3:
        r.append('{}: {:.1f}'.format(nome,sum(notas)/3))
    elif len(notas) == 4:
        notas.pop(notas.index(min(notas)))
        r.append('{}: {:.1f}'.format(nome,sum(notas)/3))

for x in r:
    print(x)