# codility word machine problem

# integer X - pushes to the stack
# POP - the machine removes the topmost number from the stack
# DUP - the machine pushes a duplicate of the topmost number of the stack
# + - the machine pops the two topmost elements from the stack and pushes in the stack their sum
# - - the machine pops the two topmost elements from the stack and pushes in the stack their difference


def solution(operations):
    stack = []
    operation_list = operations.split(' ')

    for operation in operation_list:
        if operation.isdecimal():
            stack.append(int(operation))
        elif operation == 'POP':
            if len(stack) < 1:
                raise Exception('Machine needs at least one card to perform operation.')
            stack.pop(-1)
        elif operation == 'DUP':
            if len(stack) < 1:
                raise Exception('Machine needs at least one card to perform operation.')
            stack.append(stack[-1])
        elif operation == '+':
            if len(stack) < 2:
                raise Exception('Machine needs at least two cards to perform operation.')
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            stack.append(num1 + num2)
        elif operation == '-':
            if len(stack) < 2:
                raise Exception('Machine needs at least two cards to perform operation.')
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            stack.append(num1 - num2)

    if stack:
        return stack[-1]
    raise Exception('Stack is empty.')


if __name__ == '__main__':
    print(solution(operations='13 DUP 4 POP 5 DUP + DUP + -'))
    print(solution(operations='5 6 + -'))
    print(solution(operations='3 DUP 5 - -'))
