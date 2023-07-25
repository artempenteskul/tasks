# task number - 136


from typing import List


def single_number(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num  # XOR bit operation

    return res


# solution is based on XOR bit operation which removes duplicates bits from res variable


if __name__ == '__main__':
    print(single_number([2, 2, 1]))  # 1
    print(single_number([4, 1, 2, 1, 2]))  # 4
    print(single_number([1]))  # 1
