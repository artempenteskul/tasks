# task number - 3285
# topics - array


def stable_mountains(height: list[int], threshold: int) -> list[int]:
    stables = []
    prev = 0

    for i in range(len(height)):
        if prev > threshold:
            stables.append(i)

        prev = height[i]

    return stables


if __name__ == '__main__':
    input_height = [1, 2, 3, 4, 5]
    input_threshold = 2
    print(f'Stable mountains indices for input - {stable_mountains(input_height, input_threshold)}')  # [3, 4]

    input_height = [10, 1, 10, 1, 10]
    input_threshold = 3
    print(f'Stable mountains indices for input - {stable_mountains(input_height, input_threshold)}')  # [1, 3]

    input_height = [10, 1, 10, 1, 10]
    input_threshold = 10
    print(f'Stable mountains indices for input - {stable_mountains(input_height, input_threshold)}')  # []
