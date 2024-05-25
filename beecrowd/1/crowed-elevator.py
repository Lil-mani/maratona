t = int(input())
for _ in range(t):
    n,c,m = map(int,input().split())

    # m> numero de andares c> numero de pessoas que cabe no elevadpr 

    fila = list(map(int,input().split()))
    fila.sort(reverse=True)

    i = 0
    total = 0
    while i< len(fila):
        total += fila[i] * 2

        i = i+c
    
    print(total)

