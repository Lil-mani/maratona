import sys
sys.setrecursionlimit(1000000)
def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b,(a%b))
    
t = int(input())
for _ in range(t):
    n1,n2 = map(int,input().split())
    print(mdc(n1,n2))