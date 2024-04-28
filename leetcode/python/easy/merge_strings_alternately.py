# task number - 1768


def merge_alternately(word_1: str, word_2: str) -> str:
    merge_word = ''

    min_len = min(len(word_1), len(word_2))

    for i in range(min_len):
        merge_word += word_1[i] + word_2[i]

    if len(word_1) > min_len:
        merge_word += word_1[min_len:]

    if len(word_2) > min_len:
        merge_word += word_2[min_len:]

    return merge_word


if __name__ == '__main__':
    input_word_1 = 'abc'
    input_word_2 = 'pqr'
    print(f'Alternately merge for input words - {merge_alternately(input_word_1, input_word_2)}')  # apbqcr

    input_word_1 = 'ab'
    input_word_2 = 'pqrs'
    print(f'Alternately merge for input words - {merge_alternately(input_word_1, input_word_2)}')  # apbqrs
