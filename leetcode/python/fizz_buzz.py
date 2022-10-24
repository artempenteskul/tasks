from typing import List


class Solution:
    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        res_values = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res_values.append('FizzBuzz')
            elif i % 3 == 0:
                res_values.append('Fizz')
            elif i % 5 == 0:
                res_values.append('Buzz')
            else:
                res_values.append(str(i))
        return res_values


if __name__ == '__main__':
    assert Solution.fizz_buzz(3) == ['1', '2', 'Fizz']
