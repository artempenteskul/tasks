def max_ranges_sum(arr, ranges):
    max_range_sum = sum(arr[ranges[0][0]:ranges[0][-1]+1])
    for r in ranges[1:]:
        range_sum = sum(arr[r[0]:r[-1] + 1])
        max_range_sum = max(max_range_sum, range_sum)
    return max_range_sum


if __name__ == '__main__':
    seq = [1, -2, 3, 4, -5, -4, 3, 2, 1]
    poses = [[1, 3], [0, 4], [6, 8]]
    print(max_ranges_sum(seq, poses))
