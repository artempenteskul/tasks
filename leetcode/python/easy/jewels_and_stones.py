# task number - 771


def num_of_jewels_in_stones(jewels: str, stones: str):
    jewels_set = set(jewels)
    jewels_num = 0

    for stone in stones:
        if stone in jewels_set:
            jewels_num += 1

    return jewels_num


if __name__ == '__main__':
    input_jewels = 'aA'
    input_stones = 'aAAbbbb'
    print(f'Number of jewels in stones for input - {num_of_jewels_in_stones(input_jewels, input_stones)}')  # 3

    input_jewels = 'z'
    input_stones = 'ZZ'
    print(f'Number of jewels in stones for input - {num_of_jewels_in_stones(input_jewels, input_stones)}')  # 0
