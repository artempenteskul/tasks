# task number - 412


from typing import List


def fizz_buzz(n: int) -> List[str]:
    res_values = []
    for i in range(1, n + 1):
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
    print(fizz_buzz(3))  # ['1', '2', 'Fizz']
    print(fizz_buzz(11))  # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11']
