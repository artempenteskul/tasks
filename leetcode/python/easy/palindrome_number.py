# task number - 9

class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()

    print(s.is_palindrome(121))  # True
    print(s.is_palindrome(-121))  # False
    print(s.is_palindrome(10))  # False
