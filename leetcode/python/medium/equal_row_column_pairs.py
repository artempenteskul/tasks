# task number - 2352


def equal_pairs(grid: list[list[int]]) -> int:
    rows = dict()
    for row in grid:
        r = tuple(row)
        rows[r] = rows.get(r, 0) + 1

    cols = dict()
    for i in range(len(grid)):
        c = tuple(row[i] for row in grid)
        cols[c] = cols.get(c, 0) + 1

    res = 0

    for key in rows:
        if key in cols:
            res += rows[key] * cols[key]

    return res


if __name__ == '__main__':
    input_grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(f'Quantity of equal pairs for input grid - {equal_pairs(input_grid)}')  # 1

    input_grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print(f'Quantity of equal pairs for input grid - {equal_pairs(input_grid)}')  # 3
