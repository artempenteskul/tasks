def find_anagrams(word, words):
    res = []

    word_symbols = []
    for symbol in word:
        word_symbols.append(symbol)
    word_symbols.sort()

    for item in words:
        word_letters = []
        for symbol in item:
            word_letters.append(symbol)
        word_letters.sort()
        if word_symbols == word_letters:
            res.append(item)
    return res


if __name__ == '__main__':
    print(find_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
