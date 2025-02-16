# task number - 42
# topics - array, two pointers, dynamic programming, stack, monotonic stack


def trap(height: list[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1

    left_max, right_max = height[left], height[right]

    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


if __name__ == '__main__':
    input_height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f'Trapped rain water for the input height - {trap(input_height)}')  # 6

    input_height = [4, 2, 0, 3, 2, 5]
    print(f'Trapped rain water for the input height - {trap(input_height)}')  # 9
