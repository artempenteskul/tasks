def find_non_repeating(sentence: str):
    res = ''
    index = 0
    lower_s = sentence.lower()
    for letter in lower_s:
        if lower_s.count(letter) == 1:
            res = letter
            index = lower_s.index(letter)
            break
    return sentence[index] if res else ''


if __name__ == '__main__':
    print(find_non_repeating('stress'))
    print(find_non_repeating('sTress'))
    print(find_non_repeating(''))
