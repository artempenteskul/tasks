# task number - 739
# topics - array, stack


def daily_temps(temperatures: list[int]) -> list[int]:
    days = [0] * len(temperatures)

    stack = []

    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            stack_index, stack_temp = stack.pop()
            days[stack_index] = index - stack_index

        stack.append((index, temp))

    return days


if __name__ == '__main__':
    input_temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f'Days to get warmer for input - {daily_temps(input_temps)}')  # [1, 1, 4, 2, 1, 1, 0, 0]

    input_temps = [30, 40, 50, 60]
    print(f'Days to get warmer for input - {daily_temps(input_temps)}')  # [1, 1, 1, 0]
