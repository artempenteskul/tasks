# task number - 11


def most_water_container(heights: list[int]) -> int:
    max_container = 0

    left = 0
    right = len(heights) - 1

    while left != right:
        current_container = min(heights[left], heights[right]) * (right - left)

        if current_container > max_container:
            max_container = current_container

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_container


if __name__ == '__main__':
    input_heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f'Container with most water - {most_water_container(input_heights)}')  # 49

    input_heights = [1, 1]
    print(f'Container with most water - {most_water_container(input_heights)}')  # 1
