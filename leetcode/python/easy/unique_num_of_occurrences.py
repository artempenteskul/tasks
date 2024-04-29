# task number - 1207


def unique_occurrences(arr: list[int]) -> bool:
    occurrences = {}

    for num in arr:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    if len(occurrences.values()) == len(set(occurrences.values())):
        return True

    return False


if __name__ == '__main__':
    input_arr = [1, 2, 2, 1, 1, 3]
    print(f'Is input array unique occurrences - {unique_occurrences(input_arr)}')  # true

    input_arr = [1, 2]
    print(f'Is input array unique occurrences - {unique_occurrences(input_arr)}')  # false

    input_arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(f'Is input array unique occurrences - {unique_occurrences(input_arr)}')  # true
