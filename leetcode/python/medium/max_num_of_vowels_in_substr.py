# task number - 1456


def max_vowels(s: str, k: int) -> int:
    vowels = 'aeiou'

    current_vowels_qty = 0

    for char in s[:k]:
        if char in vowels:
            current_vowels_qty += 1

    max_vowels_qty = current_vowels_qty

    for i in range(len(s) - k):
        if s[i] in vowels:
            current_vowels_qty -= 1

        if s[i+k] in vowels:
            current_vowels_qty += 1

        max_vowels_qty = max(max_vowels_qty, current_vowels_qty)

    return max_vowels_qty


if __name__ == '__main__':
    input_s = 'abciiidef'
    input_k = 3
    print(f'Max vowels in substring for input len and string - {max_vowels(input_s, input_k)}')  # 3

    input_s = 'aeiou'
    input_k = 2
    print(f'Max vowels in substring for input len and string - {max_vowels(input_s, input_k)}')  # 2

    input_s = 'leetcode'
    input_k = 3
    print(f'Max vowels in substring for input len and string - {max_vowels(input_s, input_k)}')  # 2
