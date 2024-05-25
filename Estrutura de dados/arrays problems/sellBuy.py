def SellBuy(a):
    buy = a[0]
    profit = 0
    for current in a:
        buy = min(current,buy)
        profit = max(profit,(current-buy))

    return profit

test1 = [7,2,1,4,5,6,8] # buy : 1   sell: 8   -> lucro = 7
test2 = [5,4,3,2,1]     # buy: 1    sell: 1   -> lucro = 0
test3 = [2,3,5,8,2,10]  # buy: 2    sell: 10   -> lucro = 8
print(SellBuy(test1))
print(SellBuy(test2))
print(SellBuy(test3))
