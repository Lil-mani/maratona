while True:
    try:

        a,b = map(int,input().split())
        if a==0 and b ==0:
            break
        s1 = set(x for x in input().split())
        s2 = set(x for x in input().split())

        c = 0
        if len(s1) < len(s2):
            for i in s1:
                if i not in s2:
                    c+=1
        else:
            for i in s2:
                if i not in s1:
                    c+=1

        print(c)
    except EOFError:
        break


