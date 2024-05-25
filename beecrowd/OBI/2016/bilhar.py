n = int(input())
arr = list(map(int,input().split()))
c = 0
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
        c+=2
    else:
        if dic[i] == 0:
            c+=2
            dic[i] = 1
        else:
            dic[i] = dic[i] -1  

print(c)