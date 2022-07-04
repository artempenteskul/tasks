def order_weight(string: str):
    numbers = string.split()
    numbers.sort()
    numbers.sort(key=lambda x: sum(int(k) for k in x))
    return ' '.join(numbers)


if __name__ == '__main__':
    print(order_weight('103 123 4444 99 2000'))
    print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))
