def add_binary(a: int, b: int) -> str:
    return str(bin(a + b))[2:]


if __name__ == '__main__':
    print(add_binary(1, 1))
    print(add_binary(2, 2))
