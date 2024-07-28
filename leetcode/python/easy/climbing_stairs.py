# task number - 70


def climb_stairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one


if __name__ == '__main__':
    input_n = 2
    print(f'Number of ways to climb stairs for input - {climb_stairs(input_n)}')  # 2

    input_n = 3
    print(f'Number of ways to climb stairs for input - {climb_stairs(input_n)}')  # 3

    input_n = 5
    print(f'Number of ways to climb stairs for input - {climb_stairs(input_n)}')  # 8
