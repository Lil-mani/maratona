coins = [100,50,25,10,5,1]

v = int(input())

# dp = [float("inf")] * (v+1)
# dp[0] = 0
# for i in range(v+1):
#     for j in range(6):
#         if i < coins[j]:
#             break
#         if abs(coins[j] - i)<= i:
#             dp[i] = min(dp[i],dp[abs(coins[j] - i)]+1)
# print(dp[v])


quantidade = 0 
for i in range(6):
    if v >= coins[i]:
        quantidade+= v // coins[i]
        v = v%coins[i]
print(quantidade)