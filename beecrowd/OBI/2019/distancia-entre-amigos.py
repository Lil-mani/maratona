n = int(input())
predios = list(map(int,input().split()))

maior = predios[0] # pelo menos a maior distancia vai ser a altura do primeiro predio computado
res = 0 
'''

max (h[j]+i-j) onde j é anterior a posição i 
na posição i a maior distancia possivel saindo de um predio anterior e chegando no ultimo 
distancia de um predio anterior -> h[i] + distancia até predio j 
a altura do predio atual - distancia entre os predios + distancia do predio i 
h[j] + i - j + h[i] 

'''
for i in range(1,n):
    maior+= 1  # +1 estamos considerando o custo do terrio -> na primeira chamda representa 
    #  h[0] + 1 -> altura do primeiro redio + terrio 

    # predios[i] ---> altura do predio atual 
    # maior deve representar a distancia do predio com maior distancia 
    # maior -> distancia x + altura do predio que vai dar a maior distancia 
    print("A maior distancia é ")
    print("a maior distancia ja encontrada e uma opção anterior -> ",res)
    print("ou é uma nova distancia encontrada ", maior + predios[i])
    res = max(res,maior + predios[i]) # vai ser a primeira distancia considerada -> não tenos comparação
    maior = max(maior,predios[i])  # predio atual ou predio passado + rua 

# No problema não podemos levar em conta apenas a altura dos predios -> considerar o maior predio como ponto de partida
# para a busca não vai funcionar. Pois a distancia na rua tambem vai contar para achar o caso de maximizar a distancia 
# se acontecer da maior distancia estar com um predio anterior, vamos sempre incrementar a distancia do predio anterior 
# se essa distancia não for o suficiente para desclassificar o predio atual, vamos partir do predio atual como melhor ponto 
# maior vai combinar os casos e res vai guardar a melhor opção 


print(res)
