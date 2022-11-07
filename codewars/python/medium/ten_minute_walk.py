DIRECTIONS = {'n': 1, 's': -1, 'e': 1, 'w': -1}


def is_valid_walk(walk):
    coordinates = [0, 0]
    for d in walk:
        if d in ('n', 's'):
            coordinates[0] += DIRECTIONS[d]
        elif d in ('e', 'w'):
            coordinates[1] += DIRECTIONS[d]

    if len(walk) == 10 and coordinates == [0, 0]:
        return True
    return False


if __name__ == '__main__':
    print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
