def max_sequence(arr: list):
    if len(arr) == 0:
        return 0
    elif all(x < 0 for x in arr):
        return 0

    max_till_now = arr[0]
    max_ending = 0

    for i in range(0, len(arr)):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending

    return max_till_now


if __name__ == '__main__':
    print(max_sequence([-1, -2, -3, -4]))
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
