# task number - 2559
# topics - array, string, prefix sum


def vowel_strings_old(words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_str_flags = [1 if x[0] in vowels and x[-1] in vowels else 0 for x in words]

    vowel_str_counters = []

    for query in queries:
        vowel_str_counters.append(sum(vowel_str_flags[query[0]:query[1] + 1]))

    return vowel_str_counters


def vowel_strings(words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    prefix_count = [0]
    counter = 0

    for index, word in enumerate(words):
        counter += 1 if word[0] in vowels and word[-1] in vowels else 0
        prefix_count.append(counter)

    return [prefix_count[query[1] + 1] - prefix_count[query[0]] for query in queries]


if __name__ == '__main__':
    input_words = ['aba', 'bcb', 'ece', 'aa', 'e']
    input_queries = [[0, 2], [1, 4], [1, 1]]
    print(f'Result count vowel str in ranges - {vowel_strings(input_words, input_queries)}')  # [2, 3, 0]

    input_words = ['a', 'e', 'i']
    input_queries = [[0, 2], [0, 1], [2, 2]]
    print(f'Result count vowel str in ranges - {vowel_strings(input_words, input_queries)}')  # [3, 2, 1]
