n = int(input())

telhado = list(map(int,input().split()))
i = 0
total_pulos = 0
while i < n-1:
    if i+2 >= n:
        if telhado[i+1] == 0:
                total_pulos = -1
                break
        total_pulos+=1
        i+=1
    else:
        if telhado[i+2] == 0:
            if telhado[i+1] == 0:
                total_pulos = -1
                break
            total_pulos+=1
            i+=1
        else:
            i+=2
            total_pulos+=1


print(total_pulos)
