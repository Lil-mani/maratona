while True:
    try:
        x,y = map(int,input().split())
        y = y*2
        print(x*y)
    except EOFError:
        break 