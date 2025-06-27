# task number - 728
# topics - math


def self_diving_nums(left: int, right: int) -> list[int]:
    def is_self_dividing_num(n: int) -> bool:
        for str_n in str(n):
            if int(str_n) == 0 or n % int(str_n) != 0:
                return False
        return True

    return [x for x in range(left, right + 1) if is_self_dividing_num(x)]


if __name__ == '__main__':
    input_left = 1
    input_right = 22
    print(f'List of self dividing nums in range - {self_diving_nums(input_left, input_right)}')  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    input_left = 47
    input_right = 85
    print(f'List of self dividing nums in range - {self_diving_nums(input_left, input_right)}')  # [48, 55, 66, 77]
