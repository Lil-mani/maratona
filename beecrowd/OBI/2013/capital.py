a,b,c,d = map(int,input().split())

if (a*b == c*d) or (a*c == b*d) or (a*d == b*c):
    print("S")
else:
    print("N")