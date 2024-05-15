# task number - 238


def product_except_self(nums: list[int]) -> list[int]:
    output = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4]
    print(f'Output of product except self - {product_except_self(input_nums)}')  # [24, 12, 8, 6]

    input_nums = [-1, 1, 0, -3, 3]
    print(f'Output of product except self - {product_except_self(input_nums)}')  # [0, 0, 9, 0, 0]
