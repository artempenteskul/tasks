# task number - 78
# topics - array, backtracking, bit manipulation


def determine_subsets(nums: list[int]) -> list[list[int]]:
    subs = [[]]

    for num in nums:
        subs += [sub + [num] for sub in subs]

    return subs


if __name__ == '__main__':
    input_nums = [1, 2, 3]
    print(f'Subsets for the input nums - {determine_subsets(input_nums)}')  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    input_nums = [0]
    print(f'Subsets for the input nums - {determine_subsets(input_nums)}')  # [[], [0]]
