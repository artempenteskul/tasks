# task number - 392


def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True

    s_pointer = 0

    for x in t:
        if x == s[s_pointer]:
            s_pointer += 1
            if s_pointer == len(s):
                return True

    return False


if __name__ == '__main__':
    input_s = 'abc'
    input_t = 'ahbgdc'
    print(f'Is subsequence for inputs - {is_subsequence(input_s, input_t)}')  # true

    input_s = 'axc'
    input_t = 'ahbgdc'
    print(f'Is subsequence for inputs - {is_subsequence(input_s, input_t)}')  # false

    input_s = 'b'
    input_t = 'c'
    print(f'Is subsequence for inputs - {is_subsequence(input_s, input_t)}')  # false
