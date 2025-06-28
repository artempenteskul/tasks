# task number - 77
# topics - backtracking


def combine(n: int, k: int) -> list[list[int]]:
    res = []

    def backtrack(start: int, current: list[int]) -> None:
        if len(current) == k:
            res.append(current[:])
            return

        for num in range(start, n + 1):
            current.append(num)
            backtrack(num + 1, current)
            current.pop()

    backtrack(1, [])

    return res


if __name__ == '__main__':
    input_n = 4
    input_k = 2
    print(f'Combinations - {combine(input_n, input_k)}')  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    input_n = 1
    input_k = 1
    print(f'Combinations - {combine(input_n, input_k)}')  # [[1]]
