# task number - 167
# topics - array, binary search, two pointers


def two_sum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        value = numbers[left] + numbers[right]

        if value > target:
            right -= 1
        elif value < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    input_numbers = [2, 7, 11, 15]
    input_target = 9
    print(f'Result of two sum for input - {two_sum(input_numbers, input_target)}')  # [1, 2]

    input_numbers = [2, 3, 4]
    input_target = 6
    print(f'Result of two sum for input - {two_sum(input_numbers, input_target)}')  # [1, 3]

    input_numbers = [-1, 0]
    input_target = -1
    print(f'Result of two sum for input - {two_sum(input_numbers, input_target)}')  # [1, 2]
