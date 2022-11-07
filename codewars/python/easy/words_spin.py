def spin_words(text: str):
    words = text.split()
    new_words = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        new_words.append(word)
    new_text = ' '.join(new_words)
    return new_text


if __name__ == '__main__':
    users_text = input('Enter your text: ')
    print(spin_words(users_text))
