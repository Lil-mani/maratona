def knap(values,weights,k,lookup=None):
    lookup = {} if lookup is None else lookup
    if k in lookup:
        return lookup[k]
    max_value = 0

    for i in range(len(values)):
        if weights[i] <= k:
            max_value = max(max_value,values[i]+knap(values, weights, k-weights[i], lookup))
    
    lookup[k] = max_value
    return lookup[k]
counter = 0 
while True:
    try:
        n,t = map(int,input().split())

        if n == 0 and t == 0:
            break

        counter+=1 
        tempos = []
        divertimentos = []
        for _ in range(n):
            tempo,divertimento = map(int,input().split())
            tempos.append(tempo)
            divertimentos.append(divertimento)
        
        res = knap(divertimentos,tempos,t)
        print("Instancia {}\n{}".format(counter,res))
        print()
    except EOFError:
        break

    