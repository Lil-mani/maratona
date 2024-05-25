
res = []
fatorial = [0,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000]
while True:
    try:
        palavra = input().strip()
        if palavra == "0":
            break 
        quantidade_anagramas = fatorial[len(palavra)]
        res.append(quantidade_anagramas)
        
    except EOFError:
        break 

for i in res:
    print(i)