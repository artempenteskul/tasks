# task number - 500
# topics - array, hash table, string


def find_words(words: list[str]) -> list[str]:
    kr_words = []

    keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for word in words:
        for keyboard_row in keyboard_rows:
            if all(letter.lower() in keyboard_row for letter in word):
                kr_words.append(word)
                break

    return kr_words


if __name__ == '__main__':
    input_words = ['Hello', 'Alaska', 'Dad', 'Peace']
    print(f'Keyboard row words - {find_words(input_words)}')  # ['Alaska', 'Dad']

    input_words = ['omk']
    print(f'Keyboard row words - {find_words(input_words)}')  # []

    input_words = ['adsdf', 'sfd']
    print(f'Keyboard row words - {find_words(input_words)}')  # ['adsdf', 'sfd']
