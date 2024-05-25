def euclides_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a,b,c,d = map(int,input().split())
divisor = b*d 
dividendo = ((a*d) + (c*b))
mdc = euclides_mdc(dividendo,divisor)

print(int(dividendo/mdc),int(divisor/mdc))

