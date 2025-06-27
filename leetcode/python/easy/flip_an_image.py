# task number - 832
# topics - array, two pointers, bit manipulation, matrix, simulation


def flip_and_invert_image(image: list[list[int]]) -> list[list[int]]:
    output = []

    for row in image:
        output_row = row[::-1]
        for i in range(len(output_row)):
            output_row[i] = 1 if output_row[i] == 0 else 0

        output.append(output_row)

    return output


if __name__ == '__main__':
    input_image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(f'Output flip and invert image - {flip_and_invert_image(input_image)}')  # [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
