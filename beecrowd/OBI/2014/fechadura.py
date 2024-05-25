n,m = map(int,input().split())

pinos = list(map(int,input().split()))

i = 0
counter = 0
while i+1 < n:
    if pinos[i] == m:
        i+=1
        continue
    counter += abs(pinos[i]-m)
    pinos[i+1] = pinos[i+1] + (m-pinos[i])
    pinos[i] = m
    i+=1

print(counter)
    