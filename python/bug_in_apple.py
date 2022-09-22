def sc(apple):
    for row_n, row in enumerate(apple):
        for value_n, value in enumerate(row):
            if value == 'B':
                return [row_n, value_n]
    return None


if __name__ == '__main__':
    apple_to_check = [
        ["A", "A", "A", "A", "A"],
        ["A", "B", "A", "A", "A"],
        ["A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A"]
    ]
    pos = sc(apple_to_check)
    print(pos)
