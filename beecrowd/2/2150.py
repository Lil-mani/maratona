while True:
    try:
        vogais = {x: 1 for x in input()}
        print(vogais)
        s = input()
        c = 0
        for i in s:
            if i in vogais:
                c+=1
            
        print(c)
    except EOFError:
        break