from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            result = max(result, self.largestRectangleArea(heights))

        return result

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
