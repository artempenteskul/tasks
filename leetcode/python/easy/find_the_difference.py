# task number - 389
# topics - hash table, string, bit manipulation, sorting


from collections import Counter


def find_difference(s: str, t: str) -> str:
    s_counter = Counter(s)
    t_counter = Counter(t)

    for key in t_counter:
        if (key not in s_counter) or s_counter[key] != t_counter[key]:
            return key


if __name__ == '__main__':
    input_s = 'abcd'
    input_t = 'abcde'
    print(f'The difference - {find_difference(input_s, input_t)}')  # 'e'

    input_s = ''
    input_t = 'y'
    print(f'The difference - {find_difference(input_s, input_t)}')  # 'y'
