n,m = map(int,input().split())
somacoluna = [0]*m
somalinha = []
for i in range(n):
    linha = list(map(int, input().split()))
    somalinha.append(sum(linha))
    for j in range(m):
        somacoluna[j]+=linha[j]
    
maxlinha = max(somalinha)
maxcoluna = max(somacoluna)
print(max(maxlinha,maxcoluna))