# Formula matematica = n! (total de permutações possiveis )
# Se tiver elementos repetidos  Permutação = n! / f1! , f2!, ... , fn! 
# onde fn representa os valores com caracteres repetidos 

def Permutaions(s): 
    # Array que vai armazenar o resultado 
    resultado = []
    # Array de visitados para realizar as permutações 
    visited = [False] * len(s)
    def DFS(path:list[int]):
        # Chegamos nas folhas da arvore de permutação, que é onde estão os resultados da permutação
        if len(path) == len(s):
            # Guardo as permutações feitas 
            resultado.append(path.copy())
            return 
        
        for i in range(len(s)):
            # Se é um valor que eu ha visistei, não tem porque checar esse elemento
            if visited[i]:
                continue
            # Marca como visitado e procura a permutação para os elementos seguintes 
            visited[i] = True 
            path.append(s[i])

            DFS(path)

            path.pop()
            visited[i] = False




    DFS([])
    return resultado




s = input()

print(Permutaions(s))