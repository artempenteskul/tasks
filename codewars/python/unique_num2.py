def find_uniq(arr: list):
    values = set(arr)
    for value in values:
        if arr.count(value) == 1:
            return value


if __name__ == '__main__':
    print(f'Unique num: {find_uniq([1, 1, 1, 2, 1, 1])}')
