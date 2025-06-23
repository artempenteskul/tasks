# task number - 258
# topics - math, simulator, number theory


def add_digits(num: int) -> int:
    str_num = str(num)

    while len(str_num) > 1:
        new_str_num = 0

        for n in str_num:
            new_str_num += int(n)

        str_num = str(new_str_num)

    return int(str_num)


if __name__ == '__main__':
    input_num = 38
    print(f'Result of add digits operation - {add_digits(input_num)}')  # 2

    input_num = 0
    print(f'Result of add digits operation - {add_digits(input_num)}')  # 0
