pred = 0
res = 0
flag = True 
while True:
    try:
        if flag:
            atual = int(input())
            if atual > pred:
                pred = atual
                continue
            else:
                res = pred + 1
                flag = False
        else:
            n = input()

    except EOFError: break 
if flag:
    print(pred+1)
else:
    print(res)