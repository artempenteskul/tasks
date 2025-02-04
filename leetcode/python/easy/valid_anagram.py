# task number - 242
# topics - hash table, string, sorting


from collections import Counter


def is_anagram_slow(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    input_s = 'anagram'
    input_t = 'nagaram'
    print(f'Input strings anagrams - {is_anagram(input_s, input_t)}')  # true

    input_s = 'rat'
    input_t = 'car'
    print(f'Input strings anagrams - {is_anagram(input_s, input_t)}')  # false
