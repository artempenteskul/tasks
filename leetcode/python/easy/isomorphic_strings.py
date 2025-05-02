# task number - 205
# topics - hash table, string


def is_isomorphic(s: str, t: str) -> bool:
    replaced_s = {}
    used_t = set()

    for s_letter, t_letter in zip(s, t):

        if s_letter in replaced_s:
            if replaced_s[s_letter] == t_letter:
                continue
            else:
                return False

        if t_letter in used_t:
            return False

        replaced_s[s_letter] = t_letter
        used_t.add(t_letter)

    return True


if __name__ == '__main__':
    input_s = 'egg'
    input_t = 'add'
    print(f'Are strings isomorphic - {is_isomorphic(input_s, input_t)}')  # true

    input_s = 'foo'
    input_t = 'bar'
    print(f'Are strings isomorphic - {is_isomorphic(input_s, input_t)}')  # false

    input_s = 'badc'
    input_t = 'baba'
    print(f'Are strings isomorphic - {is_isomorphic(input_s, input_t)}')  # false
