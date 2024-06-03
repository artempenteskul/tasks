# task number - 724


def pivot_index_slow(nums: list[int]) -> int:
    left = [0]
    for i in range(len(nums) - 1):
        left.append(left[-1] + nums[i])

    right = [0]
    for j in range(len(nums) - 1, 0, -1):
        print(j)
        right.append(right[-1] + nums[j])

    right.reverse()

    for k in range(len(left)):
        if left[k] == right[k]:
            return k

    return -1


def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i

        left_sum += nums[i]

    return -1


if __name__ == '__main__':
    input_nums = [1, 7, 3, 6, 5, 6]
    print(f'Pivot index for the input nums - {pivot_index(input_nums)}')  # 3

    input_nums = [1, 2, 3]
    print(f'Pivot index for the input nums - {pivot_index(input_nums)}')  # -1

    input_nums = [2, 1, -1]
    print(f'Pivot index for the input nums - {pivot_index(input_nums)}')  # 0
