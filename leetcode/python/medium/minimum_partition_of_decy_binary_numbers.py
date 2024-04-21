# task number - 1689


def min_partitions(n: str) -> int:
    max_number = 0

    for num in n:
        if int(num) > max_number:
            max_number = int(num)

    return max_number


if __name__ == '__main__':
    input_1 = '32'
    print(f'Min number of partitions for input_1 - {min_partitions(input_1)}')
    print()

    input_2 = '82734'
    print(f'Min number of partitions for input_2 - {min_partitions(input_2)}')
    print()

    input_3 = '27346209830709182346'
    print(f'Min number of partitions for input_3 - {min_partitions(input_3)}')
    print()
