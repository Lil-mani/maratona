dic = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E"
}
while True:
    try:
        n = int(input())
        if n == 0:
            break
        res = [0]*n
        for _ in range(n):
            questoes = list(map(int,input().split()))
            flag = False

            for i in range (5):
                if questoes[i] <= 127:
                    if flag:
                        res[_] = "*"
                    else:
                        res[_] = dic[i]
                        flag = True
        
        for i in res:
            print(i)
        
        del res 
    except EOFError:
        break 