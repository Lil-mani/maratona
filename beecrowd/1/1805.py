a,b = map(int,input().split())

sa = ((1+a-1)*(a-1))/2
sb = ((1+b)*b)/2
print(int(sb-sa))