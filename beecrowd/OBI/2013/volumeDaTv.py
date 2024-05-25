v,t = map(int,input().split())
volumes = list(map(int,input().split()))
acumulador = v
for i in volumes:
    if acumulador == 100 and i>0:
        continue
    elif acumulador == 0 and i<0:
        continue
    else:
        acumulador+=i
        if acumulador > 100:
            acumulador = 100
        elif acumulador < 0:
            acumulador = 0

print(acumulador)