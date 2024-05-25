while True:
    try:
        n = int(input())
        if n == 0:
            break
        sus = list(map(int,input().split()))
        aux = sus.copy()
        aux.sort(reverse=True)
        res = sus.index(aux[1]) + 1
        print(res)


    except EOFError:
        break 