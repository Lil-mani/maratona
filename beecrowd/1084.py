
while True:
    try:
        n,d = map(int,input().split())
        if n==0 and d == 0:
            break
        numero = input()
        dic = {}
        aux_sorted = sorted(numero)

        for i in range(d):
            dic[aux_sorted[i]] = dic.get(aux_sorted[i],0) + 1

        resultado = ''
        for i in numero:
            if i in dic and dic[i] != 0:
                dic[i]-=1
            else:
                resultado = resultado + i

        print(resultado)
    except EOFError:
        break

