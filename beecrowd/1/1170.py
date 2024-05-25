import sys
sys.setrecursionlimit(1000000000)
def calc(comida):
    if comida <= 1:
        return 0
    else:
        return 1 + calc(comida/2)
t = int(input())
for _ in range(t):
    n = float(input())
    res = calc(n)
    print("{} dias".format(res))