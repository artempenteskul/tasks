# task number - 39
# topics - array, backtracking


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def backtrack(pos: int, current: list[int]) -> None:
        if sum(current) == target:
            res.append(current[:])
            return

        if sum(current) > target:
            return

        for i in range(pos, len(candidates)):
            backtrack(i, current + [candidates[i]])

    backtrack(0, [])

    return res


if __name__ == '__main__':
    input_candidates = [2, 3, 6, 7]
    input_target = 7
    print(f'Combination sums - {combination_sum(input_candidates, input_target)}')  # [[2, 2, 3], [7]]

    input_candidates = [2, 3, 5]
    input_target = 8
    print(f'Combination sums - {combination_sum(input_candidates, input_target)}')  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    input_candidates = [2]
    input_target = 1
    print(f'Combination sums - {combination_sum(input_candidates, input_target)}')  # []

    input_candidates = [8, 7, 4, 3]
    input_target = 11
    print(f'Combination sums - {combination_sum(input_candidates, input_target)}')  # [[8, 3], [7, 4], [4, 4, 3]]
