# task number - 150
# topics - array, math, stack



def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = ['+', '-', '*', '/']

    for token in tokens:
        if token in operators:
            a, b = stack.pop(), stack.pop()

            if token == '+':
                stack.append(b + a)
            elif token == '-':
                stack.append(b - a)
            elif token == '*':
                stack.append(b * a)
            elif token == '/':
                stack.append(int(b / a))

        else:
            stack.append(int(token))

    return stack[0]


if __name__ == '__main__':
    input_tokens = ['2', '1', '+', '3', '*']
    print(f'Result of RPN eval - {eval_rpn(input_tokens)}')  # 9

    input_tokens = ['4', '13', '5', '/', '+']
    print(f'Result of RPN eval - {eval_rpn(input_tokens)}')  # 6

    input_tokens = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
    print(f'Result of RPN eval - {eval_rpn(input_tokens)}')  # 22
