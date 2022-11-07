def find_uniq(arr: list):
    for num in arr:
        if arr.count(num) == 1:
            return num


if __name__ == '__main__':
    print(f'Unique num: {find_uniq([1, 1, 1, 2, 1, 1])}')
    print(f'Unique num: {find_uniq([0, 0, 0.55, 0, 0])}')
