# task number - 9


def is_palindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome(121))  # True
    print(is_palindrome(-121))  # False
    print(is_palindrome(10))  # False
