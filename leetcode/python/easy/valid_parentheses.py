# task number - 20


def is_valid(s: str) -> bool:
    stack = []
    opposites = {'(': ')', '{': '}', '[': ']'}

    for symbol in s:
        if symbol in ('(', '{', '['):
            stack.append(symbol)
        else:
            if not stack:
                return False

            last_stack_element = stack.pop()

            if symbol != opposites[last_stack_element]:
                return False

    return not stack


if __name__ == '__main__':
    print(is_valid("()"))  # true
    print(is_valid("()[]{}"))  # true
    print(is_valid("(]"))  # false
    print(is_valid("([)]"))  # false
