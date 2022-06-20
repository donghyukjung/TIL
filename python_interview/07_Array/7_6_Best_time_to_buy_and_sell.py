import sys


def sol(prices : list[int])->int :
    profit=0
    min_price=sys.maxsize
    for price in prices:
        min_price=min(min_price,price)
        profit=max(profit,price-min_price)
    return profit
prices=[7,1,5,3,6,4]
print(sol(prices))