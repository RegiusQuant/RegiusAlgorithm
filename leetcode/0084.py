from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        
        stack = []
        heights.append(0)
        for height in heights:
            width = 0
            while stack and stack[-1][0] > height:
                width += stack[-1][1]
                result = max(result, stack[-1][0] * width)
                stack.pop()
            stack.append((height, width + 1))

        return result
