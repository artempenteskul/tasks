# task number - 2390


def remove_stars(s: str) -> str:
    res = ''
    for symbol in s:
        if symbol != '*':
            res += symbol
        else:
            res = res[:-1]

    return res


def remove_stars_1(s: str) -> str:
    stack = []
    for symbol in s:
        if symbol != '*':
            stack.append(symbol)
        else:
            stack.pop(-1)

    return ''.join(stack)


if __name__ == '__main__':
    input_s = 'leet**cod*e'
    print(f'Input str without stars - "{remove_stars(input_s)}"')  # 'lecoe'

    input_s = 'erase*****'
    print(f'Input str without stars - "{remove_stars(input_s)}"')  # ''
