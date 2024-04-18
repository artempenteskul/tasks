# task number - 1512


def num_of_good_pairs(nums: list[int]) -> int:
    nums_count = {}

    for n in nums:
        if n in nums_count:
            nums_count[n] += 1
        else:
            nums_count[n] = 1

    return sum([sum(range(0, nums_count[n])) for n in nums_count])


def num_of_good_pairs_1(nums: list[int]) -> int:
    ans = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] == nums[j]:
                ans += 1

    return ans


if __name__ == '__main__':
    input_1 = [1, 2, 3, 1, 1, 3]
    print(f'Number of good pairs for input {input_1} = {num_of_good_pairs(input_1)}')  # 4

    input_2 = [1, 1, 1, 1]
    print(f'Number of good pairs for input {input_2} = {num_of_good_pairs(input_2)}')  # 6
