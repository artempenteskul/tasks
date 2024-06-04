# task number - 1004


def longest_ones_slow(nums: list[int], k: int) -> int:
    longest = 0
    current = []
    zeroes = 0

    for n in nums:
        if k == 0 and n == 0:
            current = []
            continue

        if n == 0:
            if zeroes < k:
                zeroes += 1
            elif zeroes == k:
                current_first = current.pop(0)
                while current_first != 0:
                    current_first = current.pop(0)

        current.append(n)
        longest = max(longest, len(current))

    return longest


def longest_ones(nums: list[int], k: int) -> int:
    left = right = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1

        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1

    return right - left + 1


if __name__ == '__main__':
    input_nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    input_k = 2
    print(f'Max consecutive ones for the input - {longest_ones(input_nums, input_k)}')  # 6

    input_nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    input_k = 3
    print(f'Max consecutive ones for the input - {longest_ones(input_nums, input_k)}')  # 10

