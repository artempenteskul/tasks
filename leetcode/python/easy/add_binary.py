
# task number - 67

from itertools import zip_longest


def add_binary(a: str, b: str) -> str:
    a_len = len(a) - 1
    b_len = len(b) - 1

    res = ''
    head_one = 0

    while a_len >= 0 or b_len >= 0:
        total_sum = head_one

        if a_len >= 0:
            total_sum += int(a[a_len])
            a_len -= 1

        if b_len >= 0:
            total_sum += int(b[b_len])
            b_len -= 1

        res = str(total_sum % 2) + res
        head_one = total_sum // 2

    if head_one:
        res = '1' + res

    return res


if __name__ == '__main__':
    print(add_binary(a='11', b='1'))  # '100'
    print(add_binary(a='1010', b='1011'))  # '10101'
