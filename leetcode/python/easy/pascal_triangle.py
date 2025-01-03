# task number - 118
# topics - array, dynamic programming


def generate_pascal_triangle(num_rows: int) -> list[list[int]]:
    pascal_triangle = []

    for i in range(num_rows):
        if i == 0:
            current_row = [1]
        elif i == 1:
            current_row = [1, 1]
        else:
            current_row = [1]
            prev_row = pascal_triangle[i-1]

            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j-1] + prev_row[j])

            current_row.append(1)

        pascal_triangle.append(current_row)

    return pascal_triangle


if __name__ == '__main__':
    input_num_rows = 5
    print(f'Result pascal triangle rows - {generate_pascal_triangle(input_num_rows)}')
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    input_num_rows = 1
    print(f'Result pascal triangle rows - {generate_pascal_triangle(input_num_rows)}')
    # [[1]]
