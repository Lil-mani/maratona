from math import sqrt
t = int(input())

for _ in range(t):
    w,h,x0,y0 = map(int,input().split())

    xf,yf = (x0+w),(y0+h)

    type,lvl,cx,cy = input().split()
    lvl = int(lvl)
    cx = int(cx)
    cy = int(cy)

    dano = 0
    raio = 0
    if type == 'fire':
        dano = 200
        match lvl:
            case 1:
                raio = 20
            case 2:
                raio = 30
            case 3:
                raio = 50
    elif type == 'water':
        dano = 300
        match lvl:
            case 1:
                raio = 10
            case 2:
                raio = 25
            case 3:
                raio = 40
    elif type == 'earth':
        dano = 400
        match lvl:
            case 1:
                raio = 25
            case 2:
                raio = 55
            case 3:
                raio = 70
    elif type == 'air':
        dano = 100
        match lvl:
            case 1:
                raio = 18
            case 2:
                raio = 38
            case 3:
                raio = 60

    # se a distancia do centro até a ponta inferior esquerda <= raio -> atingiu
    # print(raio)
    distancia_left_down = sqrt((x0-cx)**2+(y0-cy)**2)
    print(distancia_left_down)
    distancia_left_up = sqrt((x0-cx)**2 + (yf-cy)**2)
    print(distancia_left_up)
    distancia_right_up = sqrt((xf-cx)**2+(yf-cy)**2) 
    print(distancia_right_up)
    distancia_right_down = sqrt((xf-cx)**2+(y0-cy)**2)
    print(distancia_right_down)
    if distancia_left_down > raio and distancia_left_up > raio and distancia_right_up > raio and distancia_right_down > raio:
        dano = 0
    
    print(dano)
    