while True:
    try:
        n,d = map(int,input().split())
        # n -> numero de pessoas d-> data
        data = []

        for _ in range(d):
            s = input().split()
            data.append(s)

        flag = False
        res = ''
        for i in range(d):
            prev = data[i][1]
            for j in range(1,n+1):
                if data[i][j] == '1' and data[i][j] == prev:
                    prev = '1'
                    flag = True 
                else:
                    flag = False
                    break
            if flag:
                res = data[i][0] 
                break
        
        if res != '':
            print(res)
        else:
            print('Pizza antes de FdI')

    except EOFError:
        break 
    