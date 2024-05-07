# task number - 443


# CONSTANT EXTRA SPACE


def compress(chars: list[str]) -> int:
    original_char_len = len(chars)

    prev_char = None
    counter = 0

    while original_char_len:
        if chars[0] == prev_char:
            counter += 1
        else:
            if prev_char:
                chars.append(prev_char)
                if counter > 1:
                    chars += [n for n in str(counter)]

            prev_char = chars[0]
            counter = 1

        chars.pop(0)
        original_char_len -= 1

    chars.append(prev_char)
    if counter > 1:
        chars += [n for n in str(counter)]

    return len(chars)


if __name__ == '__main__':
    input_chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    print(f'Result integer after compression - {compress(input_chars)}')  # 6
    print(f'Result input chars after compression - {input_chars}')  # ['a', '2', 'b', '2', 'c', '3']

    input_chars = ['a']
    print(f'Result integer after compression - {compress(input_chars)}')  # 1
    print(f'Result input chars after compression - {input_chars}')  # ['a']

    input_chars = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    print(f'Result integer after compression - {compress(input_chars)}')  # 4
    print(f'Result input chars after compression - {input_chars}')  # ['a', 'b', '1', '2']
