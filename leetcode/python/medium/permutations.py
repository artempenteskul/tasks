# task number - 46
# topics - array, backtracking


def permute(nums: list[int]) -> list[list[int]]:
    res = []

    def backtrack(current: list[int]):
        if len(current) == len(nums):
            res.append(current[:])
        else:
            for num in nums:
                if num not in current:
                    backtrack(current + [num])

    backtrack([])

    return res


if __name__ == '__main__':
    input_nums = [1, 2, 3]
    print(f'Permutations - {permute(input_nums)}')  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    input_nums = [0, 1]
    print(f'Permutations - {permute(input_nums)}')  # [[0, 1], [1, 0]]
