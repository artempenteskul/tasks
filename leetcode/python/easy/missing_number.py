# task number - 268


def missing_number(nums: list[int]) -> int:
    nums_set = set(nums)

    for num in range(len(nums) + 1):
        if num not in nums_set:
            return num


if __name__ == '__main__':
    input_1 = [3, 0, 1]
    output_1 = missing_number(input_1)
    print(f'Missing number from input_1 - {output_1}')

    input_2 = [0, 1]
    output_2 = missing_number(input_2)
    print(f'Missing number from input_2 - {output_2}')

    input_3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    output_3 = missing_number(input_3)
    print(f'Missing number from input_3 - {output_3}')
