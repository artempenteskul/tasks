# task number - 344
# topics - two pointers, string


def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    input_s = ['h', 'e', 'l', 'l', 'o']
    reverse_string(input_s)
    print(f'After string reverse operation: {input_s}')
