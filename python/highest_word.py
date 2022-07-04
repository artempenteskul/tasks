def high(x):
    words = x.split()
    highs = [sum([ord(x) - 96 for x in word]) for word in words]
    highest_index = highs.index(max(highs))
    highest_word = words[highest_index]
    return highest_word
