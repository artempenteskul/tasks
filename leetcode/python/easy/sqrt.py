# task number - 69


def count_sqrt(x: int) -> int:
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        candidate = mid * mid

        if candidate == x:
            return mid
        elif candidate < x:
            start = mid + 1
        elif candidate > x:
            end = mid - 1

    return end


def count_sqrt_2(x: int) -> int:
    counter = 1
    while True:
        value = counter * counter
        if value > x:
            return counter - 1
        elif value == x:
            return counter
        else:
            counter += 1


def count_sqrt_3(x: int) -> int:
    import math
    return math.floor(math.sqrt(x))


if __name__ == '__main__':
    print(count_sqrt(4))  # 2
    print(count_sqrt(8))  # 2
    print(count_sqrt(81))  # 9
    print(count_sqrt(8421))  # 91
