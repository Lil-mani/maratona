t = int(input())
for _ in range(t):
    b,h = map(int,input().split())

    res = (b*h)//2
    print("{} cm2".format(res))