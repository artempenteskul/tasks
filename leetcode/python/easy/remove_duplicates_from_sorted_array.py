# task number - 26


from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    unique_nums_qty = 0
    last_unique_num = None

    for num in nums:
        if last_unique_num != num:
            nums[unique_nums_qty] = num
            last_unique_num = num
            unique_nums_qty += 1

    return unique_nums_qty


if __name__ == '__main__':
    print(remove_duplicates_from_sorted_array([1, 1, 2]))  # 2
    print(remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5

