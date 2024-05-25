res = []
while True:
    try:
        # n = numero de tickets originais 
        # m = numero de pessoas na festa 
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        ticktes = list(map(int,input().split()))
        dic = {}
        dicFinder = {}
        counter = 0

        for i in range(m):
            if ticktes[i] not in dic:
                dic[ticktes[i]] = 1
            else:
                if ticktes[i] in dic and ticktes[i] in dicFinder:
                    continue
                else:
                    counter+=1
                    dicFinder[ticktes[i]] = 1

        res.append(counter)
    except EOFError:
        break

for i in res:
    print(i)