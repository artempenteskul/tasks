# task number - 836


def is_rectangle_overlap(rec1: list[int], rec2: list[int]) -> bool:
    return (rec1[0] < rec2[2] and rec1[1] < rec2[3]) and (rec2[0] < rec1[2] and rec2[1] < rec1[3])


if __name__ == '__main__':
    print(is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]))  # true
    print(is_rectangle_overlap([0, 0, 1, 1], [1, 0, 2, 1]))  # false
    print(is_rectangle_overlap([0, 0, 1, 1], [2, 2, 3, 3]))  # false
    print(is_rectangle_overlap([8, 7, 13, 15], [10, 8, 12, 20]))  # true
