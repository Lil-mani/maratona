t =int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    n = arr.pop(0)
    media = sum(arr)/n
    c = 0
    for i in arr:
        if i > media:  
            c+=1
    
    percentual =  (c/n) * 100
    print(f'{percentual:.3f}%')

