while True:
    try:
        n = int(input())
        arr = list(map(int,input().split()))
        cont1 = 0
        for i in arr:
            if i == 1: cont1+=1

        if cont1 >= ((2/3) * n): print("impeachment")
        else: print("acusacao arquivada")
    except EOFError:
        break