# task number - 1561


# not efficient
def max_coins_1(piles: list[int]) -> int:
    my_coins = 0

    while len(piles) != 0:
        piles.remove(max(piles))  # alice choice

        my_choice = max(piles)
        my_coins += my_choice
        piles.remove(my_choice)

        piles.remove(min(piles))  # bob choice

    return my_coins


# efficient
def max_coins_2(piles: list[int]) -> int:
    piles.sort()

    my_coins = 0

    i = 0
    j = len(piles) - 1

    while i < j:
        my_coins += piles[j - 1]
        i += 1
        j -= 2

    return my_coins


# efficient
def max_coins(piles: list[int]) -> int:
    piles.sort()

    my_coins = 0

    for i in range(len(piles) // 3, len(piles), 2):
        my_coins += piles[i]

    return my_coins


if __name__ == '__main__':
    print(f'Max coins for first input - {max_coins([2, 4, 1, 2, 7, 8])}')  # 9
    print(f'Max coins for second input - {max_coins([2, 4, 5])}')  # 4
    print(f'Max coins for third input - {max_coins([9, 8, 7, 6, 5, 1, 2, 3, 4])}')  # 18
