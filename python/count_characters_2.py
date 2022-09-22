from collections import Counter


def count_characters(string):
    return Counter(string)


if __name__ == '__main__':
    text = 'aba'
    print(count_characters(text))
