from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        values = {}
        for num_n, num in enumerate(nums):
            if target - num in values:
                return [values[target - num], num_n]
            else:
                values[num] = num_n


if __name__ == '__main__':
    print(Solution.two_sum([2, 7, 11, 15], 9))
    print(Solution.two_sum([3, 3], 6))
