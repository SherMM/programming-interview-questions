import sys
import random


def find_max_profit_bf(stocks):
    """
    docstring
    """
    best_buy, best_sell = 0, 0
    max_profit = 0
    for i in range(len(stocks)):
        buy = stocks[i]
        for j in range(i, len(stocks)):
            sell = stocks[j]
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
                best_buy = buy
                best_sell = sell
    return best_buy, best_sell


def find_max_profit(stocks):
    """
    docstring
    """
    buy, sell = stocks[0], stocks[0]
    min_price = float("inf")
    max_profit = 0
    for stock in stocks:
        profit = max(max_profit, stock - min_price)
        if profit > max_profit:
            max_profit = profit
            buy, sell = min_price, stock
        min_price = min(min_price, stock)
    return buy, sell


if __name__ == "__main__":
    n = int(sys.argv[1])
    stocks = []
    for _ in range(n):
        stocks.append(random.randrange(100, 501))

    #stocks = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] 
    buy, sell = find_max_profit(stocks)
    print(stocks)
    print(buy, sell)