# task number - 345


def reverse_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowels_order = [x for x in s if x in vowels]

    new_str = ''

    for x in s:
        new_str += vowels_order.pop(-1) if x in vowels else x

    return new_str


if __name__ == '__main__':
    input_s = 'hello'
    print(f'Result of vowels reverse - "{reverse_vowels(input_s)}"')  # "holle"

    input_s = 'leetcode'
    print(f'Result of vowels reverse - "{reverse_vowels(input_s)}"')  # "leotcede"
