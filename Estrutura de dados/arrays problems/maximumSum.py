
# função que retorna a maior soma
def maximumSum(a):
    i = 0 
    j = 0
    result = 0
    aux = 0
    while j < len(a):
        #achei um numero negativo
        if a[j] < 0:
            while i <j:
                aux-= a[i]
                i+=1
            i+=1
        
        if a[j] > 0:
            aux+= a[j]
        
        result = max(aux,result)
        j+= 1
    return result


test1 = [-15,2,3,5,6,-1,2,5] # 2+3+5+6 = 16
test2 = [20,3,4,-5,2,60] # 62
test3 = [3,6,-10,-20,4]  # 9 
print(maximumSum(test3))