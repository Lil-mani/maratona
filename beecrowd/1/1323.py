# formula -> n(n+1)(2n+1)/6
while True:
    try:
        n = int(input())
        if n == 0:
            break
        res = ((n*(n+1))*((2*n)+1))/6
        print(round(res))
    except EOFError:
        break 