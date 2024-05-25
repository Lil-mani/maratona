pula = 0
while True:
    try:
        year = int(input())
        b = 0
        flag = 1

        if pula:
            print('')
        pula = 1
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
             print("This is an leap year.")
             b = 1
             flag = 0
        if year%15 == 0:
             print('This is huluculu festival year.')
             flag = 0
        if year%55 == 0 and b:
            print('This is bulukulu festival year.')
        if flag:
            print("This is a ordinary year.")
    except EOFError:
        break 