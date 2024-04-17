# task number - 191


def hamming_weight(n: int) -> int:
    return n.bit_count()


def hamming_weight_1(n: int) -> int:
    counter = 0

    while n > 0:
        if n % 2 == 1:
            counter += 1

        n = n // 2

    return counter


if __name__ == '__main__':
    print(f'Output hamming_weight - {hamming_weight(n=11)}')  # 3
    print(f'Output hamming_weight_1 - {hamming_weight_1(n=11)}')  # 3
