# task number - 225


class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if self.empty():
            self.q1.append(x)
        else:
            for i in range(len(self.q1)):
                self.q2.append(self.q1.pop(0))

            self.q1.append(x)

            for j in range(len(self.q2)):
                self.q1.append(self.q2.pop(0))

    def pop(self) -> int or None:
        if self.empty():
            return None

        return self.q1.pop(0)

    def top(self) -> int or None:
        if self.empty():
            return None

        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == '__main__':
    my_stack = MyStack()
    my_stack.push(11)

    test_1 = my_stack.pop()
    print(f'Test 1 - {test_1}')

    test_2 = my_stack.top()
    print(f'Test 2 - {test_2}')

    test_3 = my_stack.empty()
    print(f'Test 3 - {test_3}')

    ###

    my_stack_1 = MyStack()

    my_stack_1.push(1)
    my_stack_1.push(2)
    my_stack_1.push(3)

    test_11 = my_stack_1.top()

    print(f'Test 11 - {test_11}')

    ###

    my_stack_2 = MyStack()

    my_stack_2.push(1)
    my_stack_2.push(2)

    test_21 = my_stack_2.top()
    print(f'Test 21 - {test_21}')

    test_22 = my_stack_2.pop()
    print(f'Test 22 - {test_22}')

    test_23 = my_stack_2.empty()
    print(f'Test 23 - {test_23}')
