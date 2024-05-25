# mushrooms 
import math
arr= []
for _ in range(4):
    v = input().split()
    arr.append([int(v[0]),int(v[1])])

arr.sort()
# x1 x3   
A = abs(arr[0][0]-arr[2][0])
# y1 - y3
B = abs(arr[0][1]-arr[2][1])

if B == 0:
    # o quadrado esta paralelo 
    print(A*A)
else:
    #pitagoras
    A = A*A
    print(A)
    B = B*B
    print(B)
    L = math.sqrt(A+B) # arrumar a aproximação
    print(int(L*L))

