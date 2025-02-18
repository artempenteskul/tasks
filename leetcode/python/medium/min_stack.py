# task number - 155
# topics - stack, design


class MinStack:
    def __init__(self) -> None:
        self.stack: list[tuple] = []
        self.min_val: int or None = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
        else:
            self.min_val = min(val, self.min_val)

        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_val = self.stack[-1][1] if self.stack else None

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]
