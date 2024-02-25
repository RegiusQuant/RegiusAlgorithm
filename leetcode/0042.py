from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        stack = []
        for h in height:
            width = 0
            while stack and stack[-1][0] < h:
                bottom = stack[-1][0]
                width += stack[-1][1]
                stack.pop()

                if not stack:
                    break
                up = min(h, stack[-1][0])
                result += width * (up - bottom)
            stack.append((h, width + 1))

        return result