def move_zeros(seq: list):
    nums = []
    zeros = []
    for i in seq:
        zeros.append(i) if i == 0 else nums.append(i)
    return nums + zeros


if __name__ == '__main__':
    print(move_zeros(seq=[1, 0, 1, 2, 0, 1, 3]))
