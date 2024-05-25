while True:
    try:
        n = int(input())
        arr = []

        for _ in range(n):
            i,f = map(int,input().split())
            arr.append([i,f])

        arr.sort(key = lambda x: x[1])
        c = 0
        k = 0
        for i in range(n):
            if arr[i][0] > k:
                k= arr[i][1]
                c+=1

        print(c)
    except EOFError:
        break
    