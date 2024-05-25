array = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]

while True:
    try:
        mes, dia = map(int, input().split())
        if mes == 12 and dia == 25:
            print("E natal!")
        elif mes == 12 and dia == 24:
            print("E vespera de natal!")
        elif mes == 12 and dia > 25:
            print("Ja passou!")
        else:
            x = array[mes - 1] - dia
            for i in range(mes, 12):
                x += array[i]
            
            print("Faltam {} dias para o natal!".format(x))
    except EOFError:
        break
