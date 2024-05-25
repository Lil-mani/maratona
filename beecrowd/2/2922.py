while True:
    try:
        B,U = map(int,input().split())
        if B > U:
            print(B-U-1)
        elif B< U:
            print(U-B-1)
        else:
            print(0)
    except EOFError:
        break 