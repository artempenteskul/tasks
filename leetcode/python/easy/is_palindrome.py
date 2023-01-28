class Solution:
    def is_palindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()

    print(s.is_palindrome(121))
    print(s.is_palindrome(-121))
    print(s.is_palindrome(10))
