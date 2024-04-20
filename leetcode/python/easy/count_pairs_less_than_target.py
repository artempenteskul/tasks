# task number - 2824


def count_pairs(nums: list[int], target: int) -> int:
    counter = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                counter += 1
    return counter


if __name__ == '__main__':
    input_nums = [-1, 1, 2, 3, 1]
    input_target = 2
    print(f'Number of pairs less than target for inputs: {count_pairs(input_nums, input_target)}')  # 3
