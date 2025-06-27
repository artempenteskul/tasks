# task number - 657
# topics - string, simulation


def judge_circle(moves: str) -> bool:
    origin = [0, 0]

    for move in moves:
        if move == 'U':
            origin[0] += 1
        elif move == 'D':
            origin[0] -= 1
        elif move == 'R':
            origin[1] += 1
        elif move == 'L':
            origin[1] -= 1

    return origin[0] == 0 and origin[1] == 0


if __name__ == '__main__':
    input_moves = 'UD'
    print(f'Has robot returned to origin - {judge_circle(input_moves)}')  # true

    input_moves = 'LL'
    print(f'Has robot returned to origin - {judge_circle(input_moves)}')  # false
