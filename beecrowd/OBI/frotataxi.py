pa,pg,ka,kg  = map(float,input().split())


g = ka/pa
a = kg/pg
a = round(a,4)
g = round(g,4)

if a < g:
    print("A")
else:
    print("G")
