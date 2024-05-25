def combine(scores:list[int],ages:list[int])->int:
    # age scores é uma array que combina o scores e ages e forma ordenada 
    # ordenação de forma crescente 
    ages_scores = sorted(zip(ages,scores),key= lambda x: (x[0],x[1]))

    # teams é uma array que vai ser utilizada para guardar o valor das combinações possiveis de times 
    Teams= [0]*len(scores)
    for i in range(len(ages_scores)):
        # O primeiro valor possivel para um time com a pessoa i 
        # é o score da propria pessoa i
        Teams[i] = ages_scores[i][1] 

        # Começo fazer as combinações a partir da pessoa i
        for j in range(i):
            # Se o score de uma pessoa mais velha for maior que o score de uma pessoa mais nova
            # Não temos conflitos e podemos formar grupos com o jogador j e jogador i
            if ages_scores[i][1]>= ages_scores[j][1]:
                Teams[i]= max(Teams[i],ages_scores[i][1]+Teams[j])
    return max(Teams)



scores = [4,5,6,5]
ages = [2,1,2,1]
print(combine(scores,ages))