# task number - 202


def is_happy(num: int) -> bool:
    visited_nums = set()

    while num not in visited_nums:
        visited_nums.add(num)
        num = count_sum_of_squares(num)

        if num == 1:
            return True

    return False


def count_sum_of_squares(n: int) -> int:
    """
    this is algorithm to iterate through integer
    """
    res = 0
    while n:
        digit = n % 10
        res += digit ** 2
        n = digit // 10

    return res


#############

def is_happy_2(num: int) -> bool:
    visited_nums = set()

    while num not in visited_nums:
        visited_nums.add(num)

        local_num = 0
        for digit in str(num):
            local_num += int(digit) ** 2

        if local_num == 1:
            return True

        num = local_num

    return False


if __name__ == '__main__':
    print(is_happy(num=19))  # true
    print(is_happy(num=2))  # false
    print(is_happy(num=1))  # true
