# task number - 1


from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    values = {}

    for num_index, num_value in enumerate(nums):
        if target - num_value in values:
            return [values[target - num_value], num_index]
        else:
            values[num_value] = num_index


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 3], 6))  # [0, 1]
    print(two_sum([2, 7, 11, 15, 3], 14))  # [2, 4]
