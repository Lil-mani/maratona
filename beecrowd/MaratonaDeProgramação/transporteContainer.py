a,b,c = map(int,input().split())
x,y,z = map(int,input().split())

if a > x or b>y or c>z:
    print("0")
else:
    limitex = x//a
    limitey = y//b
    limitez = z//c

    resposta = limitex * limitey * limitez
    print(resposta)