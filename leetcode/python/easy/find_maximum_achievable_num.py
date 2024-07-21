# task number - 2769


def maximum_achievable_num(num: int, t: int) -> int:
    return num + t * 2


if __name__ == '__main__':
    input_num = 4
    input_t = 1
    print(f'Maximum achievable num - {maximum_achievable_num(input_num, input_t)}')  # 6

    input_num = 3
    input_t = 2
    print(f'Maximum achievable num - {maximum_achievable_num(input_num, input_t)}')  # 7
