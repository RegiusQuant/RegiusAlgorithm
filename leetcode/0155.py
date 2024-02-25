class MinStack:

    def __init__(self):
        self.stack = []
        self.record = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.record:
            self.record.append(val)
        else:
            self.record.append(min(self.record[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.record.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.record[-1]
