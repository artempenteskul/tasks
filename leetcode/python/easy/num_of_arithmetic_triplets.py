# task number - 2367


def arithmetic_triplets_num(nums: list[int], diff: int) -> int:
    n = len(nums)

    triplets_counter = 0

    for i in range(n):
        for j in range(i+1, n):
            if nums[j] - nums[i] != diff:
                continue
            for k in range(j+1, n):
                if nums[k] - nums[j] == diff:
                    triplets_counter += 1

    return triplets_counter


if __name__ == '__main__':
    input_nums = [0, 1, 4, 6, 7, 10]
    input_diff = 3
    print(f'Num of arithmetic triplets for nums and diff is: {arithmetic_triplets_num(input_nums, input_diff)}')  # 2

    input_nums = [4, 5, 6, 7, 8, 9]
    input_diff = 2
    print(f'Num of arithmetic triplets for nums and diff is: {arithmetic_triplets_num(input_nums, input_diff)}')  # 2
