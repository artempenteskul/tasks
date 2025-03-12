# task number - 999
# topics - array, matrix, simulation


def num_rook_pawn_captures(board: list[list[str]]) -> int:

    available_pawn_captures = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':

                rook_row = board[i]

                for x in range(i - 1, -1, -1):
                    if rook_row[x] == 'p':
                        available_pawn_captures += 1
                    elif rook_row[x] == 'B':
                        break

                for x in range(i + 1, 8):
                    if rook_row[x] == 'p':
                        available_pawn_captures += 1
                    elif rook_row[x] == 'B':
                        break

                rook_column = [c[j] for c in board]

                for x in range(j - 1, -1, -1):
                    if rook_column[x] == 'p':
                        available_pawn_captures += 1
                    elif rook_column[x] == 'B':
                        break

                for x in range(j + 1, 8):
                    if rook_column[x] == 'p':
                        available_pawn_captures += 1
                    elif rook_column[x] == 'B':
                        break

    return available_pawn_captures


if __name__ == '__main__':
    input_board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print(f'Number of available rook pawn captures - {num_rook_pawn_captures(input_board)}')  # 3

    input_board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "B", "R", "B", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print(f'Number of available rook pawn captures - {num_rook_pawn_captures(input_board)}')  # 0

