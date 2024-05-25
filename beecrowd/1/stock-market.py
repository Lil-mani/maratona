import sys

n, c = map(int, input().split())
prices = list(map(int, input().split()))

ans = 0
ax = -sys.maxsize

for v in prices:
    pr = ans
    ans = max(ans, ax + v)
    ax = max(ax, pr - v - c)

print(ans)