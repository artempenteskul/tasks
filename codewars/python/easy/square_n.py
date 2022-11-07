def square_sum(numbers: list):
    res = 0
    for num in numbers:
        res += num ** 2
    return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(square_sum(nums))
