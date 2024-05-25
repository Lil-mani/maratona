import math
n,l,d = map(int,input().split())
num1 = n*(d/1000)
num2 = num1/l
num2 = math.ceil(num2)
print(num2*l)