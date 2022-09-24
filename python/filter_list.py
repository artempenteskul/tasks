def filter_list(seq: list):
    return list(filter(lambda x: type(x) == int, seq))


if __name__ == '__main__':
    s = [1, 2, 'aasf', '1', '123', 123]
    print(filter_list(seq=s))
