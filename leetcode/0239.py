from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        queue = deque()
        for i, x in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < x:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
