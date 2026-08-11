class MinStack:

    def __init__(self):
        self.min_history = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_history:
            self.min_history.append(min(self.min_history[-1], val))
        else:
            self.min_history.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.min_history.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_history[-1]
