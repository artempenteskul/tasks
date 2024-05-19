# task number - 1679


from collections import Counter


def max_operations(nums: list[int], k: int) -> int:
    counter = 0
    nums_dict = Counter(nums)
    checked = set()

    for num in nums_dict:
        if num not in checked:
            if k / 2 == num:
                counter += nums_dict[num] // 2
            else:
                if k - num in nums_dict:
                    counter += min(nums_dict[num], nums_dict[k - num])
                    checked.add(k - num)

            checked.add(num)

    return counter


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4]
    input_k = 5
    print(f'Output pairs qty of k num from inputs - {max_operations(input_nums, input_k)}')  # 2

    input_nums = [3, 1, 3, 4, 3]
    input_k = 6
    print(f'Output pairs qty of k num from inputs - {max_operations(input_nums, input_k)}')  # 1
