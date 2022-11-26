def is_narcissistic(value):
    digits_sum = 0
    for digit in str(value):
        digits_sum += pow(int(digit), len(str(value)))

    return True if digits_sum == value else False


if __name__ == '__main__':
    print(is_narcissistic(7))
    print(is_narcissistic(371))
    print(is_narcissistic(4887))
