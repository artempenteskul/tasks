# task number - 999
# topics - array, matrix, simulation


def num_rook_pawn_captures(board: list[list[str]]) -> int:

    available_pawn_captures = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':

                rook_row = board[i]
                rook_column = [r[j] for r in board]

                for x in reversed(rook_row[:j]):
                    if x == 'p':
                        available_pawn_captures += 1
                        break
                    elif x == 'B':
                        break

                for x in rook_row[j:]:
                    if x == 'p':
                        available_pawn_captures += 1
                        break
                    elif x == 'B':
                        break

                for x in reversed(rook_column[:i]):
                    if x == 'p':
                        available_pawn_captures += 1
                        break
                    elif x == 'B':
                        break

                for x in rook_column[i:]:
                    if x == 'p':
                        available_pawn_captures += 1
                        break
                    elif x == 'B':
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

    input_board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "B", "B", "B", "B", "B", "."],
        [".", "p", "B", "p", "p", "p", "B", "p"],
        [".", "p", "B", "p", "R", "p", "B", "p"],
        [".", "p", "B", "p", "p", "p", "B", "p"],
        [".", ".", "B", "B", "B", "B", "B", "."],
        [".", ".", ".", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print(f'Number of available rook pawn captures - {num_rook_pawn_captures(input_board)}') # 4

