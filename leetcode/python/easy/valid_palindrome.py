# task number - 125


def is_palindrome(s: str) -> bool:
    clean_s = ''
    for symbol in s:
        if symbol.isalnum():
            clean_s += symbol.lower()

    return True if clean_s == clean_s[::-1] else False


if __name__ == '__main__':
    print(is_palindrome('A man, a plan, a canal: Panama'))  # true
    print(is_palindrome('race a car'))  # false
    print(is_palindrome(' '))  # true
