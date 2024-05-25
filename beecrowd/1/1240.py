t = int(input())
for i in range(t):
    n1,n2 = input().split()
    tam = len(n2)
    n1 = int(n1)
    n2 = int(n2)
    if n1 < n2:
        print("nao encaixa")
    else:
        mult = 1
        while tam>0:
            mult *= 10
            tam-=1
        aux = n1 % (mult)
        if aux == n2:
            print('encaixa')
        else:
            print('nao encaixa')
