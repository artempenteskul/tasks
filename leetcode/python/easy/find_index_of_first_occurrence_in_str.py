# task number - 28

def find_first_occurrence_in_str(haystack: str, needle: str) -> int:
    for letter_index, letter in enumerate(haystack):
        if letter == needle[0]:
            if haystack[letter_index: letter_index + len(needle)] == needle:
                return letter_index
    return -1


if __name__ == '__main__':
    print(find_first_occurrence_in_str(haystack='sadbutsad', needle='sad'))  # 0
    print(find_first_occurrence_in_str(haystack='sdadbutsad', needle='sad'))  # 7
    print(find_first_occurrence_in_str(haystack='leetcode', needle='leeto'))  # -1
