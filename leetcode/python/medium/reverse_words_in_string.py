# task number - 151


def reverse_words(s: str) -> str:
    words = [word for word in s.split() if word]
    return ' '.join(reversed(words))


if __name__ == '__main__':
    input_s = 'the sky is blue'
    print(f'Output of input string after reverse_words: "{reverse_words(input_s)}"')  # "blue is sky the"

    input_s = '  hello world  '
    print(f'Output of input string after reverse_words: "{reverse_words(input_s)}"')  # "world hello"

    input_s = 'a good   example'
    print(f'Output of input string after reverse_words: "{reverse_words(input_s)}"')  # "example good a"
