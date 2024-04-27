# task number - 2942


def find_words_with_letter(words: list[str], x: str) -> list[int]:
    return [index for index in range(len(words)) if x in words[index]]


if __name__ == '__main__':
    input_words = ['leet', 'code']
    input_x = 'e'
    print(f'Result for words {input_words} and x {input_x} is {find_words_with_letter(input_words, input_x)}')  # [0, 1]

