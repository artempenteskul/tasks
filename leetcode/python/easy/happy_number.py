# task number - 202


def is_happy(num: int) -> bool:
    nums = set()
    nums.add(num)

    while True:
        local_num = 0
        for digit in str(num):
            local_num += int(digit) ** 2

        if local_num == 1:
            return True
        elif local_num in nums:
            return False

        nums.add(local_num)
        num = local_num


if __name__ == '__main__':
    print(is_happy(num=19))  # true
    print(is_happy(num=2))  # false
