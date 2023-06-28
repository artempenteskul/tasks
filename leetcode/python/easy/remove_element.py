# task number - 27


from typing import List


def remove_element(nums: List[int], val: int) -> int:
    counter = 0

    for num in nums:
        if num != val:
            nums[counter] = num
            counter += 1

    return counter


if __name__ == '__main__':
    print(remove_element([3, 2, 2, 3], 3))  # 2
    print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5

