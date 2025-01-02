# task number - 121
# topics - array, dynamic programming


def max_profit(prices: list[int]) -> int:
    profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price

        if price > min_price:
            profit = max(profit, price - min_price)

    return profit


if __name__ == '__main__':
    input_prices = [7, 1, 5, 3, 6, 4]
    print(f'Max profit on stock with input prices - {max_profit(input_prices)}')  # 5

    input_prices = [7, 6, 4, 3, 1]
    print(f'Max profit on stock with input prices - {max_profit(input_prices)}')  # 0
