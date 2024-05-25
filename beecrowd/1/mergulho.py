while True:
    try:
        n,r = map(int,input().split())
        arr = list(map(int,input().split()))
        dic = {}
        for i in arr:
            dic[i] = 1
        missing = []

        for i in range(1,n+1):
            if i not in dic:
                missing.append(i)

        if len(missing) > 0:
            for i in range(len(missing)):
                print(missing[i],end=" ")
            print()
        else: 
            print("*")
    except EOFError:
        break 