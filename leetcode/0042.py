from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        leftPtr, rightPtr = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        while leftPtr < rightPtr:
            leftMax = max(leftMax, height[leftPtr])
            rightMax = max(rightMax, height[rightPtr])
            
            if leftMax < rightMax:
                result += leftMax - height[leftPtr]
                leftPtr += 1
            else:
                result += rightMax - height[rightPtr]
                rightPtr -= 1

        return result
