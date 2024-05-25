m,s = map(int,input().split())
minimo = float("inf")
acumulador = s

for _ in range(m):
    value = int(input())
    acumulador+=value
    minimo = min(minimo,acumulador)

print(minimo)