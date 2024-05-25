x01,y01,x11,y11 = map(int,input().split())
x02,y02,x12,y12 =  map(int,input().split())

if x12 >= x01 and x02 <=x11 and y12 >= y01 and y02 <= y11:
    print("1")
else:
    print("0")