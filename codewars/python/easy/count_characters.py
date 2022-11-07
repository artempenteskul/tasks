def count_characters(string: str) -> dict:
    characters = {}
    for c in string:
        if c not in characters:
            characters[c] = string.count(c)

    return {} if len(string) == 0 else characters


if __name__ == '__main__':
    text = 'aba'
    print(count_characters(text))
