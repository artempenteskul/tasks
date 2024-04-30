# task number - 394

def decode_string(s: str) -> str:
    stack = []
    for symbol in s:
        if symbol == ']':
            part = ''
            while stack[-1] != '[':
                part = stack.pop() + part

            stack.pop()

            digit = ''
            while stack and stack[-1].isdigit():
                digit = stack.pop() + digit

            stack.append(part * int(digit))

        else:
            stack.append(symbol)

    return ''.join(stack)


if __name__ == '__main__':
    input_s = '3[a]2[bc]'
    print(f'Decode string output - "{decode_string(input_s)}"')  # "aaabcbc"

    input_s = '3[a2[c]]'
    print(f'Decode string output - "{decode_string(input_s)}"')  # "accaccacc"

    input_s = '2[abc]3[cd]ef'
    print(f'Decode string output - "{decode_string(input_s)}"')  # "abcabccdcdcdef"

    input_s = '11[a]'
    print(f'Decode string output - "{decode_string(input_s)}"')  # "aaaaaaaaaaa"
