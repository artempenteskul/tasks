# task number - 3190
# topics - array, math


def min_operations(nums: list[int]) -> int:
    counter = 0

    for num in nums:
        if num % 3 != 0:
            counter += 1

    return counter


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4]
    print(f'Min operations to make all input nums divisible by three - {min_operations(input_nums)}')  # 3

    input_nums = [3, 6, 9]
    print(f'Min operations to make all input nums divisible by three - {min_operations(input_nums)}')  # 0
