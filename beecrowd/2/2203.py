from math import sqrt
while True:
    try:
        xf,yf,xi,yi,vi,r1,r2 = map(int,input().split())

        
        hipo = sqrt((xf-xi)**2+(yf-yi)**2)
        hipo+= vi*1.50
        if hipo < (r1+r2):
            print('Y')
        else:
            print('N')
    except EOFError:
        break