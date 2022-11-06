from typing import List, Union
from math import sqrt


def is_square(arr: List) -> Union[bool, None]:
    if len(arr) == 0:
        return None
    if all(sqrt(x) == int(sqrt(x)) for x in arr):
        return True
    return False


if __name__ == '__main__':
    print(is_square([1, 4, 9, 16]))
    print(is_square([3, 4, 7, 9]))
