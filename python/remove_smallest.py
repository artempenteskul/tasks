def remove_smallest(numbers: list):
    if len(numbers) == 0:
        return []

    numbers_copy = numbers[:]
    smallest_number = min(numbers_copy)
    del numbers_copy[numbers_copy.index(smallest_number)]
    return numbers_copy


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(remove_smallest(nums))
