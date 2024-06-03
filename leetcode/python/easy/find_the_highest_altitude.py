# task number - 1732


def highest_altitude(gain: list[int]) -> int:
    highest = 0
    prev = 0

    for g in gain:
        prev += g
        highest = max(highest, prev)

    return highest


if __name__ == '__main__':
    input_gain = [-5, 1, 5, 0, -7]
    print(f'Highest altitude for the input gain - {highest_altitude(input_gain)}')  # 1

    input_gain = [-4, -3, -2, -1, 4, 3, 2]
    print(f'Highest altitude for the input gain - {highest_altitude(input_gain)}')  # 0

