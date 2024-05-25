counter = 0
while True:
    try:
        a,v = map(int,input().split())   
        counter+=1
        if a==0 and v == 0:
            break
        fluxo = [0]*a
        maior = 0
        for _ in range(v):
            u,v = map(int,input().split()) 
            fluxo[u-1]+=1
            fluxo[v-1]+=1
            maior = max(maior,fluxo[u-1],fluxo[v-1])

        print("Teste",counter)
        for i in range(0,a):
            if fluxo[i] == maior:
                print(i+1,end=" ")
        print()
        print()
        del fluxo
    except EOFError: break


