# task number - 374


def guess_api(pick: int) -> int:
    # returns 0 if pick is correct
    # returns 1 if pick is higher
    # returns -1 if pick is lower
    pass


def guess_num(n: int) -> int:
    left = 1
    right = n

    while left <= right:
        middle = (left + right) // 2
        guess_res = guess_api(middle)

        if guess_res == 0:
            return middle
        elif guess_res == 1:
            left = middle + 1
        else:
            right = middle - 1
