t = int(input())

for _ in range(t):
    s = input().split()
    s1 = s[0]
    s2 = s[1]
    resultante = s1[0]
    i = 1
    j = 0
    while i < len(s1) and j < len(s2):
        if i>j:
            resultante = resultante + s2[j]
            j+=1
        else:
            resultante = resultante + s1[i]
            i+=1

    while i < len(s1):
        resultante = resultante + s1[i]
        i+=1


    while j < len(s2):
        resultante = resultante + s2[j]
        j+=1
        # print(j,len(s2))

    print(resultante)