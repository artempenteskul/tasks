# task number - 1476


class SubRectangleQueries:
    def __init__(self, rectangle: list[list[int]]) -> None:
        self.rectangle = rectangle

    def update_rectangle(self, row_1: int, col_1: int, row_2: int, col_2: int, new_value: int) -> None:
        for i in range(row_1, row_2 + 1):
            for j in range(col_1, col_2 + 1):
                self.rectangle[i][j] = new_value

    def get_value(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


if __name__ == '__main__':
    input_1 = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    sub_rectangle_queries = SubRectangleQueries(rectangle=input_1)

    output_get_value = sub_rectangle_queries.get_value(1, 1)
    print(f'Get value output - {output_get_value}')

    print(f'Current rectangle - {sub_rectangle_queries.rectangle}')

    sub_rectangle_queries.update_rectangle(0, 0, 3, 2, 5)
    print(f'Current rectangle after update - {sub_rectangle_queries.rectangle}')
