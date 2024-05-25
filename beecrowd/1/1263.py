
while True:
    try:
        s = input().split()
        prev = s[0][0].lower()
        flag = False
        count = 0
        for i in range(1,len(s)):
            if s[i][0].lower() == prev and not flag:
                count+=1
                flag = True 
            elif s[i][0].lower() != prev:
                prev = s[i][0].lower()
                flag = False

        print(count)
    except EOFError:
        break 