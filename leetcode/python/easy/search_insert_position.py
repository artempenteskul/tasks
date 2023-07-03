# task number - 35


from typing import List


def search_insert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1

        if nums[mid] > target:
            high = mid

    return low


def search_insert_2(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return low


if __name__ == '__main__':
    print(search_insert([1, 3, 5, 6], 5))  # 2
    print(search_insert([1, 3, 5, 6], 2))  # 1
    print(search_insert([1, 3, 5, 6], 7))  # 4
    print(search_insert([1, 3, 5, 6], -1))  # 0
