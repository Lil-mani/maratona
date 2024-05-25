import math

INF = math.inf

n, S = map(int, input().split())

w = [0] * (n + 1)
v = [0] * (n + 1)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    w[i] = b
    v[i] = a


dp = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
opt = [
    [False for _ in range(S + 1)] for _ in range(n + 1)
]  # opt[i][j] = o i-ésimo item será escolhido no subconjunto ótimo de dp[i][j] ou não

dp[0][0] = 0

for i in range(1, S + 1):
    dp[0][i] = -INF

for i in range(1, n + 1):
    for j in range(1, S + 1):
        if w[i] > j:
            opt[i][j] = False
            dp[i][j] = dp[i - 1][j]
        else:
            if (
                dp[i - 1][j] <= dp[i - 1][j - w[i]] + v[i]
            ):  # A melhor opção é pegar o i-ésimo item
                opt[i][j] = True
                dp[i][j] = dp[i - 1][j - w[i]] + v[i]
            else:  # A melhor opção é não pegar o i-ésimo item
                opt[i][j] = False
                dp[i][j] = dp[i - 1][j]

s = 0
# ÍNdice que maximiza dp[n][s]
answer = 0

items = []

for i in range(i, S + 1):
    if answer < dp[n][i]:
        s = i
        answer = dp[n][i]

for i in range(n, 0, -1):
    if opt[i][s]:  # Nós usamos o item i na resposta ótima
        s -= w[i]
        items.append(i)

items.reverse()  # Revertendo a resposta para ela ficar em ordem crescente

print(f"Maximal sum of values: {answer}")

print("Items of the optimal subset:")

print(*items)
