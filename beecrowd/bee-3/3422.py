n = int(input())
respostas = []
for _ in range(n):
    minuto, tempo = input().split()
    minuto = int(minuto)
    if tempo == '1T':
        if minuto > 45:
            respostas.append('{}+{}'.format(45,minuto-45))
        else:
            respostas.append('{}'.format(minuto))
    elif tempo == '2T':
        if minuto > 45:
            respostas.append('{}+{}'.format(90,minuto-45))
        else:
            respostas.append('{}'.format(minuto+45))
for x in respostas:
    print(x)