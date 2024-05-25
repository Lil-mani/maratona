'''
 problema: reconhecer os elementos "leaders"  de uma array /// leader = elemento maior que todos os elementos a direita dele 


    [4, 7, 1, 0]
    0   1  2  3

    [5,2,1,3,10,4,3,5]

    algoritmo: passa pela array e empilha se o elemento cumprir as caracteristicas de um leader
    se o topo da pilha for menor do que algum elemento seguinte, passa pela stack tirando os valores
    que não são leaders :d
'''
def leadersArray(a)->list: 
    stack = [a[0]]
    for i in range(1,len(a)):
        if a[i] >= stack[len(stack)-1]:
            while len(stack) > 0 and a[i] >= stack[len(stack)-1]:
                stack.pop()
        stack.append(a[i])
    
    return sorted(stack)

test1 = [4,7,1,0]
test2 = [5,2,1,3,10,4,3,5]
test3 = [10, 22, 12, 3, 0, 6]
test4 = [1,2,2,1]
test5 = [187,64,133,62,49,163,50 ,115 ,42 ,65 ,60 ,49 ,32 ,87 ,141 ,142 ,146 ,159]

print(leadersArray(test5))