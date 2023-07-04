# task number - 66


from typing import List


def plus_one(digits: List[int]) -> List[int]:
    head_one, index = 1, -1

    for d in digits[::-1]:
        if head_one:
            if d == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                head_one = 0
        else:
            break

        index -= 1

    if head_one:
        digits.insert(0, 1)

    return digits


if __name__ == '__main__':
    print(plus_one([1, 2, 3]))  # [1, 2, 4]
    print(plus_one([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(plus_one([9]))  # [1, 0]
    print(plus_one([9, 9, 9]))  # [1, 0, 0, 0]
