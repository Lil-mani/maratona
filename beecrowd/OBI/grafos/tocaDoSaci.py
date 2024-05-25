from queue import SimpleQueue
n,m = map(int,input().split()) # Dimensão do labirinto 
mat = [[0 for x in range(m)] for y in range(n)] #matriz do labirinto 
# Coordenadas do meu ponto inicial 
x_incial = 0
y_inicial = 0
# Coordenadas do meu ponto final 
x_final = 0
y_final = 0

for i in range(n):
    mat[i] = [int(x)  for x in input().split()]
    for j in range (m):
        if mat[i][j] == 2:
            x_incial = i
            y_inicial = j
        if mat[i][j] == 3:
            x_final = i
            y_final = j

# Resolvendo o labirinto 
distancia = [[0 for x in range(m)] for y in range(n)]
visitados = [[False for x in range(m)] for y in range(n)]
distancia[x_incial][y_inicial] = 1
visitados[x_incial][y_inicial] = True

dx = [+1,-1,0,0] # movimenta norte - sul 
dy = [0,0,+1,-1] # movimenta leste-oeste 

# Filas para fazer a busca -> São sincronizadas 
fila_x = SimpleQueue() 
fila_y = SimpleQueue() 
fila_x.put(x_incial)
fila_y.put(y_inicial)
sz = 1 # variavel para marcar a camada sendo explorada 

while not fila_x.empty():
    # tira o começo da fila para explorar se existe um caminho
    x = fila_x.get() 
    y = fila_y.get()
    sz-= 1 

    # Vamos procurar o caminho que pode ser explorado 
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        # Se as coordenadas novas não estiverem dentro da matriz
        # não é possivel explorar esses pontos 
        if a<0 or b<0: continue
        if a>=n or b>=m: continue
        if mat[a][b] == 0 or visitados[a][b] == True: continue
        # Incrementamos a distancia percorrida baseado no tanto que já andamos
        distancia[a][b] = distancia[x][y] + 1
        visitados[a][b] = True
        # Empilhamos esse caminho
        fila_x.put(a)
        fila_y.put(b)
        sz+=1 # Se é um caminho possivel, é uma camada a mais a ser explorada 

print(distancia[x_final][y_final])

