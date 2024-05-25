from queue import SimpleQueue
n,m = map(int,input().split())
mat = [[0 for x in range(m)] for y in range(n)] #matriz do labirinto 
# Coordenadas do ponto inicial 
x_inicio = 0
y_inicio = 0

x_final = 0
y_final = 0

for i in range(n):
    mat[i] = [int(x)  for x in input().split()]
    for j in range (m):
        if mat[i][j] == 3:
            x_inicio = i
            y_inicio = j

# Resolvendo o labirinto 
distancia = [[0 for x in range(m)] for y in range(n)]
visitados = [[False for x in range(m)] for y in range(n)]
# distancia[x_inicio][y_inicio] = 1
visitados[x_inicio][y_inicio] = True
# Fila para varrer o labirinto 
fila_x = []
fila_y = []
# Arrays de movimento 
dx = [+1,-1,0,0]
dy = [0,0,+1,-1]

sz = 1 # variavel para controlar a camada 

fila_x.append(x_inicio)
fila_y.append(y_inicio)

find_exit = False

while len(fila_y) > 0:
    x = fila_x[0]
    y = fila_y[0]

    del fila_x[0]
    del fila_y[0]
    sz-=1

    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if a<0 or b<0: continue
        if a>=n or b>=m: continue
        if mat[a][b] == 2 or visitados[a][b] == True: continue # Uma sala com cristal não vai ser visitada
        if mat[a][b] == 0:
            find_exit = True 
            distancia[a][b] = distancia[x][y] + 1 
            x_final = a
            y_final = b
            break
        # Incrementamos a distancia percorrida baseado no tanto que já andamos
        distancia[a][b] = distancia[x][y] + 1
        visitados[a][b] = True
        fila_x.append(a)
        fila_y.append(b)
        sz+=1

    if find_exit:
        break

print(distancia[x_final][y_final])


