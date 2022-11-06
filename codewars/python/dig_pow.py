def dig_pow(n: int, p: int) -> int:
    digits = list(map(int, list(str(n))))
    sum_digits = 0
    for d in digits:
        sum_digits += d ** p
        p += 1

    if sum_digits / n == int(sum_digits / n):
        return int(sum_digits / n)
    return -1


if __name__ == '__main__':
    print(dig_pow(695, 2))
    print(dig_pow(46288, 3))
    print(dig_pow(92, 1))
