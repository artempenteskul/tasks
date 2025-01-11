# task number - 2894
# topics - math


def difference_of_slow(n: int, m: int) -> int:
    num1 = sum([x for x in range(1, n + 1) if x % m != 0])
    num2 = sum([y for y in range(1, n + 1) if y % m == 0])
    return num1 - num2


def difference_of_sums(n: int, m: int) -> int:
    num1 = 0
    num2 = 0

    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
        else:
            num1 += i

    return num1 - num2


if __name__ == '__main__':
    input_n = 10
    input_m = 3
    print(f'Difference between divisible and non divisible sums - {difference_of_sums(input_n, input_m)}')  # 19

    input_n = 5
    input_m = 6
    print(f'Difference between divisible and non divisible sums - {difference_of_sums(input_n, input_m)}')  # 15
