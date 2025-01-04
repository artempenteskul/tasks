# task number - 169
# topics - array, hash table, divide and conquer, sorting, counting


def majority_element(nums: list[int]) -> int:
    seen = {}
    seen_max = None
    seen_max_counter = 0

    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

        if seen[num] > seen.get(seen_max, 0):
            seen_max = num
            seen_max_counter = seen_max_counter

    return seen_max


if __name__ == '__main__':
    input_nums = [3, 2, 3]
    print(f'Result majority element for input nums - {majority_element(input_nums)}')  # 3

    input_nums = [2, 2, 1, 1, 1, 2, 2]
    print(f'Result majority element for input nums - {majority_element(input_nums)}')  # 2
