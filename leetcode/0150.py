from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                x, y = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                z = self.calculate(x, y, token)
                stack.append(z)
            else:
                stack.append(int(token))
        return stack[0]
    
    def calculate(self, x: int, y: int, op: str) -> int:
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return int(x / y)
        return 0
