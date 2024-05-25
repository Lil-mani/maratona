def mdc(a,b):
    if b==0:
        return a
    else:
        return mdc(b,(a%b))

while True:
    try:
        x,y,z = sorted(map(int,input().split()))
        if z**2 == x**2 + y**2:
            if mdc(x,y) == 1 and mdc(y,z) == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break 