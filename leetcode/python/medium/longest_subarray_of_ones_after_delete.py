# task number - 1493


# TODO: check how this works as it was solved by luck with algo from #1004 task

def longest_subarray(nums: list[int]) -> int:
    left = right = 0
    k = 1

    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1

        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

    return right - left



if __name__ == '__main__':
    input_nums = [1, 1, 0, 1]
    print(f'Longest subarray after one deletion for input - {longest_subarray(input_nums)}')  # 3

    input_nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(f'Longest subarray after one deletion for input - {longest_subarray(input_nums)}')  # 5

    input_nums = [1, 1, 1]
    print(f'Longest subarrary after one deletion for input - {longest_subarray(input_nums)}')  # 2
