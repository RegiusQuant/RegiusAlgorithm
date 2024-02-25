from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        tokens, ops = [], []

        number = ""
        for c in s:
            if c.isdigit():
                number += c
                continue
            else:
                if number:
                    tokens.append(number)
                    number = ""

            if c == " ":
                continue

            while ops and self.getRank(ops[-1]) >= self.getRank(c):
                tokens.append(ops.pop())
            ops.append(c)

        if number:
            tokens.append(number)
        while ops:
            tokens.append(ops.pop())

        return self.evalRPN(tokens)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                x, y = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                z = self.getResult(x, y, token)
                stack.append(z)
            else:
                stack.append(int(token))
        return stack[0]

    def getRank(self, op: str) -> int:
        if op in "*/":
            return 2
        if op in "+-":
            return 1
        return 0

    def getResult(self, x: int, y: int, op: str) -> int:
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return int(x / y)
        return 0
