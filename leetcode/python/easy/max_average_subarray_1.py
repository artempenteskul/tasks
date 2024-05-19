# task number - 643


def find_max_average(nums: list[int], k: int) -> float:
    n = len(nums)

    if k == 1:
        return max(nums)

    if n == k:
        return sum(nums) / k

    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)

    return max_sum / k


if __name__ == '__main__':
    input_nums = [1, 12, -5, -6, 50, 3]
    input_k = 4
    print(f'Max average subarray for inputs - {find_max_average(input_nums, input_k)}')  # 12.75

    input_nums = [5]
    input_k = 1
    print(f'Max average subarray for inputs - {find_max_average(input_nums, input_k)}')  # 5.0

    input_nums = [0, 4, 0, 3, 2]
    input_k = 1
    print(f'Max average subarray for inputs - {find_max_average(input_nums, input_k)}')  # 4.0

    input_nums = [4, 2, 1, 3, 3]
    input_k = 2
    print(f'Max average subarray for inputs - {find_max_average(input_nums, input_k)}')  # 3.0
