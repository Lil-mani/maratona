V, n = map(int, input().split())

M = list(map(int, input().split()))

dp = [False] * (V + 1)
dp[0] = True

for i in range(n):
    for k in range(V - M[i], -1, -1):
        if dp[k]:
            dp[k + M[i]] = True

if dp[V]:
    print("S")
else:
    print("N")
