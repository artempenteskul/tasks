# task number - 807


def max_increase_keeping_skyline(grid: list[list[int]]) -> int:
    n = len(grid)
    max_increase = 0

    for i in range(n):
        for j in range(n):
            max_increase += min(max(x for x in grid[i]), max(x[j] for x in grid)) - grid[i][j]

    return max_increase


if __name__ == '__main__':
    input_grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(f'Maximum increase to keep city skyline for the input = {max_increase_keeping_skyline(input_grid)}')  # 35

    input_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(f'Maximum increase to keep city skyline for the input = {max_increase_keeping_skyline(input_grid)}')  # 0
