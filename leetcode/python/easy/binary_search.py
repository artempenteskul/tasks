# task number - 704
# topics - array, binary search


def b_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        index = (left + right) // 2
        value = nums[index]

        if value == target:
            return index
        elif value > target:
            right = index - 1
        elif value < target:
            left = index + 1

    return -1


if __name__ == '__main__':
    input_nums = [-1, 0, 3, 5, 9, 12]
    input_target = 9
    print(f'Binary search result index - {b_search(input_nums, input_target)}')  # 4

    input_nums = [-1, 0, 3, 5, 9, 12]
    input_target = 2
    print(f'Binary search result index - {b_search(input_nums, input_target)}')  # -1
