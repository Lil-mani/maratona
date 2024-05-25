a,b = map(int,input().split())
if b>0:
    r = a%b
else:
    r = a% (b*-1)
q = int((a-r)/b)

print(q,r)