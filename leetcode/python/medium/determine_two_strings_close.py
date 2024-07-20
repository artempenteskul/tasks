# task number - 1657

from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    dict1 = Counter(word1)
    dict2 = Counter(word2)

    return (
        len(word1) == len(word2) and Counter(dict1.values()) == Counter(dict2.values()) and set(dict1) == set(dict2)
    )


if __name__ == '__main__':
    input_word1 = 'abc'
    input_word2 = 'bca'
    print(f'Input strings are close - {close_strings(input_word1, input_word2)}')  # true

    input_word1 = 'a'
    input_word2 = 'aa'
    print(f'Input strings are close - {close_strings(input_word1, input_word2)}')  # false

    input_word1 = 'cabbba'
    input_word2 = 'abbccc'
    print(f'Input strings are close - {close_strings(input_word1, input_word2)}')  # true
