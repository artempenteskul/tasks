# task number - 334

import math


def increasing_triplet(nums: list[int]) -> bool:
    first = math.inf
    second = math.inf

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4, 5]
    print(f'Input nums has increasing triplet - {increasing_triplet(input_nums)}')  # true

    input_nums = [5, 4, 3, 2, 1]
    print(f'Input nums has increasing triplet - {increasing_triplet(input_nums)}')  # false

    input_nums = [2, 1, 5, 0, 4, 6]
    print(f'Input nums has increasing triplet - {increasing_triplet(input_nums)}')  # true
