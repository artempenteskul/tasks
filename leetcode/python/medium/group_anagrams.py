# task number - 49
# topics - array, hash table, string, sorting


def group_anagrams(strs: list[str]) -> list[list[str]]:
    mapping = dict()

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in mapping:
            mapping[sorted_s] += [s]
        else:
            mapping[sorted_s] = [s]

    return list(mapping.values())


if __name__ == '__main__':
    input_strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(f'Output of group anagrams flow - {group_anagrams(input_strs)}')  # [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]

    input_strs = ['a']
    print(f'Output of group anagrams flow - {group_anagrams(input_strs)}')  # [['a']]
