# R,C =   R -> numero de linhas C-> numero de colunas 
# m = []  construir a matriz 
# sr,sc = vai representar as coordenadas do start point
# rq,cq = vão ser as filas rq (row queue) cq(column queue)

#Variaveis que vão ser utilizadas para manter o traço de passos dados
# move_count = 0
# nodes_left_in_layer = 1
# nodes_in_next_layer = 0

# Variaveis usadas para manter rastro se chegamos na saida 
# reached_end = False -> se não houver saida saberemos pois não mudara seu estado

# R X C matriz para manter os nodes que foram visitados, logo caminhos que foram feitos
# vai representar que na posição (i,j) foi visitada
# visitados = [[] * x for x in range(C)]*R

# Arrays de movimento
# dr = [-1,+1,0,0] Movimenta sul-norte 
# dc = [0,0,-1,+1] Movimenta leste-oeste

# function solve():
# rq.enqueue(sr)
# cq.enqueue(sc)
# visited[sr][sc] = True 

# obs sobre o uso das filas: temos duas filas para manter o traço em x e y para melhor entendimento, 
# mas elas vão fucnionar no codigo como uma pilha só, sempre que uma fila for alterada alteramos a outra junto
# são finlas sincronizadas 

# while len(rq) > 0  -> pode utilizar a outra filas tambem, para saber se elas estão vazias 
#     r = rq.dequeu() valor do i 
#     c = rd.dequeu() valor do j 
#     se essas coordenadas forem iguais as coordenadas da saida
#     if m[r][c] == "E":
#         reached_end = true 
#         break  -> esse break quebra o laço do while e finaliza a busca 
#     explore_neighbours(r,c) -> é uma função que coloca todos os vizinhos na fila 
#     nodes_left_in_layer------
#     if node_left_in_layer == 0:
#         nodes_left_in_layer = nodes_in_next_layer
#         nodes_in_next_layer = 0
#         move_count++

# if reached_end -> se a flag que representa se chegamos no final é true. Vamos retornar o preço do caminho percorrido 
#     return move_count 
# return -1 -> não foi possivel achar uma saida 
# Função para controlar os vizinhos das celulas 
# function explore_neighbours(r,c):
#     for i in range 4
#         rr = r + dr[i]
#         cc = c + dc[i]
#         Temos que checar os casos em que os vizinhos não são valores validos 
#         if rr<0 or cc<0: continue -> chegamos nos limites negativos da matriz 
#         if rr>=R or cc>= C: continue -> chegamos nos limites positivos da matriz 

#         if visited[rr][cc]: continue -> esse é um caminho que ja foi explorado 
#         if m[rr][cc] == "#": continue -> o caminho é igual a uma pedra, e não é um caminho livre 

#         Se é um caminho valido a ser seguido, podemos empilhas esses caminhos para serem explorados 
#         rq.enqueu(rr)
#         cq.enqueu(cc)
#         visited[rq][cq] -> como é uma busca em largura, chegamos nos vizinhos e vamos marca-los como visitados
#         nodes_in_next_layer+= 1 -> incrementamos a quantidade de caminhos a serem explorados
#         -> estamos sempre nos movimentando por camadas na busca em largura. Por isso incrementa 1, nos exploramos uma nova camada 


        