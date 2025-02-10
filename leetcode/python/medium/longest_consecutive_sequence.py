# task number - 128
# topics - array, hash table, union find


def longest_consecutive(nums: list[int]) -> int:
    longest = 0
    nums = set(nums)

    for num in nums:
        if num - 1 in nums:
            continue

        current_longest = 0
        while num in nums:
            num += 1
            current_longest += 1

        longest = max(longest, current_longest)

    return longest


if __name__ == '__main__':
    input_nums = [100, 4, 200, 1, 3, 2]
    print(f'Longest consecutive sequence len - {longest_consecutive(input_nums)}')  # 4

    input_nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f'Longest consecutive sequence len - {longest_consecutive(input_nums)}')  # 9
