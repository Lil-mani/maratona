import math
# A-> volume B-> largura  C-> comprimento
A,B,C = sorted(map(int,input().split()))
H,L = sorted(map(int,input().split()))

if A<=H and B<=L:
    print('S')
else:
    print('N')