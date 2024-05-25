def cheapFlight( n: int, flights: list[list[int]], src: int, dst: int, k: int):
    prices = [float('inf')] * n
    prices[src] = 0

    for i in range(k+1):
        tmpPrices = prices[::]

        for s,d,p in flights:

         tmpPrices[d] = min(tmpPrices[d],prices[s] + p)  
        prices = tmpPrices

    return -1 if prices[dst] == float('inf') else prices[dst]



n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0 
dst = 3
k = 1

# 4
# [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
# 0
# 3
# 1

print(cheapFlight(n,flights,src,dst,k))