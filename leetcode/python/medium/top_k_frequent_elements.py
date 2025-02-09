# task number - 347
# task number - array, hash table, sorting


from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    frequency = Counter(nums)
    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_frequency.keys())[:k]


if __name__ == '__main__':
    input_nums = [1, 1, 1, 2, 2, 3]
    input_k = 2
    print(f'Output top k frequent elements - {top_k_frequent(input_nums, input_k)}')  # [1, 2]

    input_nums = [1]
    input_k = 1
    print(f'Output top k frequent elements - {top_k_frequent(input_nums, input_k)}')  # [1]

    input_nums = [4, 1, -1, 2, -1, 2, 3]
    input_k = 2
    print(f'Output top k frequent elements - {top_k_frequent(input_nums, input_k)}')  # [2, -1]
