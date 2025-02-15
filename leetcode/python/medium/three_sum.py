# task number - 15
# topics - array, two pointers, sorting


def three_sum_brute(nums: list[int]) -> list[list[int]]:
    result = set()
    nums.sort()

    for x in range(len(nums)):
        if nums[x] > 0:
            continue
        for y in range(x + 1, len(nums)):
            for z in range(y + 1, len(nums)):
                if nums[x] + nums[y] + nums[z] == 0:
                    result.add((nums[x], nums[y], nums[z]))

    return [list(r) for r in result]


def three_sum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for index, x in enumerate(nums):
        if x > 0:
            break

        if index > 0 and x == nums[index - 1]:
            continue

        left, right = index + 1, len(nums) - 1

        while left < right:
            value = x + nums[left] + nums[right]
            if value > 0:
                right -= 1
            elif value < 0:
                left += 1
            else:
                result.append([x, nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return result


if __name__ == '__main__':
    input_nums = [-1, 0, 1, 2, -1, -4]
    print(f'Result "three sum" for input - {three_sum(input_nums)}')  # [[-1, -1, 2], [-1, 0, 1]]

    input_nums = [0, 1, 1]
    print(f'Result "three sum" for input - {three_sum(input_nums)}')  # []

    input_nums = [0, 0, 0]
    print(f'Result "three sum" for input - {three_sum(input_nums)}')  # [0, 0, 0]
