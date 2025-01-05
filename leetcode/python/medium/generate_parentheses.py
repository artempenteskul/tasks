# task number - 22
# topics - string, dynamic programming, backtracking


def generate_parenthesis(n: int) -> list[str]:
    variants = [('(', 1)]

    for _ in range(n * 2 - 1):
        updated_variants = []
        for variant_value, variant_counter in variants:
            # ( case
            if variant_counter + 1 <= n:
                updated_variants.append((variant_value + '(', variant_counter + 1))

            # ) case
            if variant_counter - 1 >= 0:
                updated_variants.append((variant_value + ')', variant_counter - 1))

        variants = updated_variants

    return [x[0] for x in variants if x[1] == 0]


if __name__ == '__main__':
    input_n = 3
    print(f'Result generated parenthesis for input - {generate_parenthesis(input_n)}')
    # ['((()))', '(()())', '(())()', '()(())', '()()()']

    input_n = 1
    print(f'Result generated parenthesis for input - {generate_parenthesis(input_n)}')
    # ['()']
