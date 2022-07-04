punctuation_marks = ('!', ':', ',', '?')


def pig_it(text):
    words = text.split()
    res_words = []
    for word in words:
        if word in punctuation_marks:
            res_words.append(word)
        else:
            res_word = word[1:] + word[0] + 'ay'
            res_words.append(res_word)
    return ' '.join(res_words)


if __name__ == '__main__':
    users_text = (input('Enter your text: '))
    print(pig_it(users_text))
