def loc(x,y,n,m):
    """
    Refazer, divisa é para quando ele esta na linha do plano cartesiano
    """
    if x == n or y == m:
        return "divisa"
    # Northeastern 
    elif x > n and y > m:
        return "NE"
    # Northwestern
    elif x < n and y > m:
        return "NO"
    # Southwestern
    elif x < n and y < m:
        return "SO"
    else:
        return "SE"
    
res = []
while True:
    try:
        testCases = int(input())
        if testCases == 0:
            break 
        n,m = map(int,input().split())

        for _ in range(testCases): 
            x,y = map(int,input().split())
            res.append(loc(x,y,n,m))
            
    except EOFError:
        break

for i in res:
    print(i)