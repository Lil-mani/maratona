n = int(input())
search = n ** 2
flag = False
somacoluna = [0] * n
somalinha = []
diagonal = 0

for i in range(n):
    linha = list(map(int, input().split()))
    acm = 0
    for j in range(n):  # Corrigir o loop para calcular a soma da diagonal
        somacoluna[j] += linha[j]
        acm += linha[j]
        if i == j:  # Adicionar soma para a diagonal
            diagonal += linha[j]
    somalinha.append(acm)
    if linha.count(search) > 0:
        flag = True

if flag:
    res = diagonal
    for i in range(n):
        # Verificar se a soma da linha e da coluna é igual à soma da diagonal
        if somalinha[i] != somacoluna[i] or somalinha[i] != diagonal:
            res = 0
            break

    print(res)
else:
    print("-1")
