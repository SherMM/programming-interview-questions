import sys
import random


def find_max_profit(stocks):
    """
    docstring
    """
    max_profit = float("-inf")
    first_buy, second_buy = None, None
    first_sell, second_sell = None, None
    first_buy_sell = find_daily_max_first_profits(stocks)
    next_buy_sell = find_daily_max_second_profits(stocks)
    for t1, t2 in zip(first_buy_sell, next_buy_sell):
        buy1, sell1, profit1 = t1
        buy2, sell2, profit2 = t2
        profit = max(max_profit, profit1 + profit2)
        if profit > max_profit:
            max_profit = profit 
            first_buy, second_buy = buy1, buy2
            first_sell, second_sell = sell1, sell2
    return first_buy, first_sell, second_buy, second_sell, max_profit



def find_daily_max_first_profits(stocks):
    """
    docstring
    """
    profits = []
    buy, sell = stocks[0], stocks[0]
    min_price, max_profit = float("inf"), 0
    for stock in stocks:
        min_price = min(min_price, stock)
        profit = max(max_profit, stock - min_price)
        if profit > max_profit:
            max_profit = profit
            buy, sell = min_price, stock
        profits.append((buy, sell, max_profit))
    return profits

def find_daily_max_second_profits(stocks):
    """
    docstring
    """
    profits = []
    buy, sell = stocks[-1], stocks[-1]
    max_price = float("-inf")
    max_profit = 0
    for stock in reversed(stocks):
        max_price = max(max_price, stock)
        profit = max(max_profit, max_price - stock)
        if profit > max_profit:
            max_profit = profit
            buy, sell = stock, max_price
        profits.append((buy, sell, max_profit))
    return profits[::-1]


if __name__ == "__main__":
    n = int(sys.argv[1])
    stocks = []
    for _ in range(n):
        stocks.append(random.randrange(100, 501))
    #stocks = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print(stocks)
    print(find_max_profit(stocks))