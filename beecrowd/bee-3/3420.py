import math

def form(c):
    a = 3
    b = 1
    c_ = -c * 2

    dis = b**2 - 4*a*c_

    if dis >= 0:
        raiz1 = (-b + math.sqrt(dis)) / (2*a)
        raiz2 = (-b - math.sqrt(dis)) / (2*a)
    
    return raiz1, raiz2

t = int(input())
res = []
for i in range(1,t+1):
    c = int(input())
    if c>=2:
        n1,n2 = form(c)
        n1 = int(n1)
        res.append(n1)
    else:
        res.append(0)

for i in range(t):
    print(res[i])