
import math
import sys
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())

if k == 1:
    print(n)

elif k >= math.ceil(math.log2(n)):
    print(math.ceil(math.log2(n)))

else:
    x = math.ceil(math.log2(n))  
    x = x - k - 1  
    x = 2 ** x  
    print(x + k)  




