# task number - 217
# topics - array, hash table, sorting


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False


if __name__ == '__main__':
    input_nums = [1, 2, 3, 1]
    print(f'Contains duplicate - {contains_duplicate(input_nums)}')  # true

    input_nums = [1, 2, 3, 4]
    print(f'Contains duplicate - {contains_duplicate(input_nums)}')  # false

    input_nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f'Contains duplicate - {contains_duplicate(input_nums)}')  # true
