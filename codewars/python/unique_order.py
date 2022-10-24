def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    res = [iterable[0]]
    for item in iterable[1:]:
        if item != res[-1]:
            res.append(item)
    return res


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
