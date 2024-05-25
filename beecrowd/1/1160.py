import math
t = int(input())

for _ in range(t):
    pa,pb,g1,g2 = map(float,input().split())

    anos = 0

    while True:
        anos+=1
        pa += int(pa*g1)
        pb += int(pb*g2)

        if pa> pb or anos>100:
            break 


    
    if anos> 100:
        print('Mais de 1 seculo')
    else:
        print('{} anos.'.format(anos))