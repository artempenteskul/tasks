def product_fib(prod: int) -> list:
    fib_num_1 = 0
    fib_num_2 = 1
    while True:
        if fib_num_1 * fib_num_2 == prod:
            return [fib_num_1, fib_num_2, True]
        elif fib_num_1 * fib_num_2 > prod:
            return [fib_num_1, fib_num_2, False]
        else:
            fib_num_1_value = fib_num_1
            fib_num_1 = fib_num_2
            fib_num_2 += fib_num_1_value


if __name__ == '__main__':
    print(product_fib(4895))
    print(product_fib(5895))
