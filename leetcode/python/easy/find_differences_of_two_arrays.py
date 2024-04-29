# task number - 2215


def find_difference(nums_1: list[int], nums_2: list[int]) -> list[list[int]]:
    return [list(set(nums_1) - set(nums_2)), list(set(nums_2) - set(nums_1))]


if __name__ == '__main__':
    input_nums_1 = [1, 2, 3]
    input_nums_2 = [2, 4, 6]
    print(f'Difference between two input arrays: {find_difference(input_nums_1, input_nums_2)}')  # [[1, 3], [4, 6]]

    input_nums_1 = [1, 2, 3, 3]
    input_nums_2 = [1, 1, 2, 2]
    print(f'Difference between two input arrays: {find_difference(input_nums_1, input_nums_2)}')  # [[3], []]
