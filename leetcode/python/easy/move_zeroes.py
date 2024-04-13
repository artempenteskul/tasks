# task number - 283


def move_zeroes(nums: list[int]) -> None:
    last_zero_pointer = None

    for i in range(len(nums)):

        if nums[i] == 0 and last_zero_pointer is None:
            last_zero_pointer = i

        if nums[i] != 0 and last_zero_pointer is not None:
            nums[last_zero_pointer], nums[i] = nums[i], nums[last_zero_pointer]
            last_zero_pointer += 1


if __name__ == '__main__':
    input_1 = [0, 1, 0, 3, 12]
    move_zeroes(input_1)
    print(f'Input 1 after move_zeroes - {input_1}')

    input_2 = [0]
    move_zeroes(input_2)
    print(f'Input 2 after move_zeroes - {input_2}')

    input_3 = [1]
    move_zeroes(input_3)
    print(f'Input 3 after move_zeroes - {input_3}')
