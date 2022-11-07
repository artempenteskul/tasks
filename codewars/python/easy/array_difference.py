def array_diff(a: list, b: list):
    res = []
    for element in a:
        if element not in b:
            res.append(element)
    return res


if __name__ == '__main__':
    print(array_diff([1, 2], [1]))
    print(array_diff([1, 2, 2], [2]))
    print(array_diff([1, 2, 3], [1, 2]))
