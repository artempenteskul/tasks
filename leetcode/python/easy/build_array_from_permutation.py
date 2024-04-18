# task number - 1920

def build_array(nums: list[int]) -> list[int]:
    return [nums[nums[n]] for n in range(len(nums))]


if __name__ == '__main__':
    input_1 = [0, 2, 1, 5, 3, 4]
    output = build_array(input_1)
    print(f'Output for input_1 - {output}')  # [0, 1, 2, 4, 5, 3]
