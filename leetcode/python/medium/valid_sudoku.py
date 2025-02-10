# task number - 36
# topics - array, hash table, matrix


from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    boxes = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            box_key = (i // 3, j // 3)

            if num in rows[i] or num in cols[j] or num in boxes[box_key]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            boxes[box_key].add(num)

    return True


if __name__ == '__main__':
    input_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print(f'Is input sudoku valid - {is_valid_sudoku(input_board)}')  # true
