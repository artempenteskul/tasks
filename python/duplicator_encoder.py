def duplicate_encoder(text: str):
    res = ''
    text_lower = text.lower()
    for letter in text_lower:
        if text_lower.count(letter) == 1:
            res += '('
        elif text_lower.count(letter) > 1:
            res += ')'
    return res


if __name__ == '__main__':
    users_text = input('Enter your text: ')
    print(duplicate_encoder(text=users_text))
