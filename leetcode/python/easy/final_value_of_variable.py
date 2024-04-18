# task number - 2011


def final_value_after_operations(operations: list[str]) -> int:
    return sum(1 if '+' in op else -1 for op in operations)


if __name__ == '__main__':
    input_1 = ['--X', 'X++', 'X++']
    output_1 = final_value_after_operations(input_1)
    print(f'Final X value after all operations from input = {output_1}')  # 1
