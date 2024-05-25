while True:
    try:
        n = int(input())
        res = int(n / 100)
        if  n%100 > 0:
            print(res+1)
        else:
            print(res)
    except EOFError:
        break