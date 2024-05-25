r,l = map(int,input().split())
p = 3.1415

v = ((r**3)*p * 4)/3
res = int(l//v)
print(res)