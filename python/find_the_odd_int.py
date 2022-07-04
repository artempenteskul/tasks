def find_odd_int(arr: list):
    odd_int = 0
    for i in arr:
        if arr.count(i) % 2 == 1:
            odd_int = i
    return odd_int


if __name__ == '__main__':
    print(find_odd_int(arr=[7]))
    print(find_odd_int(arr=[1, 1, 2]))
    print(find_odd_int(arr=[2, 2, 6, 6, 6]))
