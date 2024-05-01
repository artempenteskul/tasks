# task number - 338


def count_bits(n: int) -> list[int]:
    return [num.bit_count() for num in range(n + 1)]


if __name__ == '__main__':
    input_n = 2
    print(f'Output of bits counting - {count_bits(n=input_n)}')  # [0, 1, 1]

    input_n = 5
    print(f'Output of bits counting - {count_bits(n=input_n)}')  # [0, 1, 1, 2, 1, 2]
