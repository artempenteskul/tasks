# task number - 290
# topics - hash table, string


def word_pattern(pattern: str, s: str) -> bool:
    if len(pattern) != len(s.split(' ')):
        return False

    mapping = {}
    used_letters = set()

    for word, letter in zip(s.split(' '), pattern):
        if word not in mapping:
            if letter not in used_letters:
                mapping[word] = letter
                used_letters.add(letter)
            else:
                return False

        else:
            if mapping[word] != letter:
                return False

    return True


if __name__ == '__main__':
    input_pattern = 'abba'
    input_s = 'dog cat cat dog'
    print(f'Is word pattern correct - {word_pattern(input_pattern, input_s)}')  # true

    input_pattern = 'abba'
    input_s = 'dog cat cat fish'
    print(f'Is word pattern correct - {word_pattern(input_pattern, input_s)}')  # false

    input_pattern = 'abba'
    input_s = 'dog dog dog dog'
    print(f'Is word pattern correct - {word_pattern(input_pattern, input_s)}')  # false
