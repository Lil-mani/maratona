"""
Dado um set de numeros, inteiros ou uma string, retornar todos os subsets prossiveis 
 Obs: um subset não pode conter duplicatas 

 exemplo: 
    nums = [1,2,3] # O total de subsets é igual a 2^n, podemos tabular de forma binaria 
    []
    [3]
    [2]
    [2,3]
    [1]
    [1,3]
    [1,2]
    [1,2,3] 
    -> 2^3 = 8 combinações possiveis sem repetição 


"""
def allSubsequences(nums):
    result = []
    partial = []

    def directed_powerset(ind):
        if ind == len(nums):
            result.append(partial[:]) # guarda as combinações feitas em resultados 
            return 
        
        partial.append(nums[ind])   
        directed_powerset(ind + 1) # Segue as combinações com o elemento 
        partial.pop() # tira o elemento para poder combinar sem esse elemento 
        directed_powerset(ind+1) # segue as combinações sem o elemento 
        
    directed_powerset(0)  # Começamos do primeiro endereço 
    return result