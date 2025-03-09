# task number - 219
# topics - array, hash table, sliding window


def contains_nearby_duplicates(nums: list[int], k: int) -> bool:
    seen = {}

    for index, num in enumerate(nums):
        if num not in seen:
            seen[num] = index
        else:
            seen_index = seen[num]

            if abs(seen_index - index) <= k:
                return True

            seen[num] = index

    return False


if __name__ == '__main__':
    input_nums = [1, 2, 3, 1]
    input_k = 3
    print(f'Does contain nearby duplicates - {contains_nearby_duplicates(input_nums, input_k)}')  # true

    input_nums = [1, 0, 1, 1]
    input_k = 1
    print(f'Does contain nearby duplicates - {contains_nearby_duplicates(input_nums, input_k)}')  # true

    input_nums = [1, 2, 3, 1, 2, 3]
    input_k = 2
    print(f'Does contain nearby duplicates - {contains_nearby_duplicates(input_nums, input_k)}')  # false
