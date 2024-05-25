n,v = map(int,input().split())
dic = {}
for _ in range(n):
    entrada = input().split()
    num_piloto = int(entrada.pop(0))
    tempo_total=0
    melhor=float('inf')
    for num in entrada:
        tempo = list(map(int,num.split(':')))
        minuto = tempo[0] * 60 * 1000
        segundo = tempo[1] * 1000
        mili = tempo[2] 
        total = minuto+segundo+mili
        tempo_total+=total
        if total < melhor:
            melhor = total
    dic[num_piloto] = [tempo_total,melhor]

sorted_grid = sorted(dic.items(),key=lambda x : x[1])

lista_melhor = []
melhor_volta = []

for i in range(len(sorted_grid)):
    lista_melhor.append([sorted_grid[i][0] , sorted_grid[i][1][0]])
    melhor_volta.append([sorted_grid[i][0] ,sorted_grid[i][1][1]])

melhor_volta = sorted(melhor_volta, key=lambda x : x[1])
res = 0
for i in range(10):
    if melhor_volta[0][0] == lista_melhor[i][0]:
        res = melhor_volta[0][0]

if res == 0:
    res = 'NENHUM'
print(res)