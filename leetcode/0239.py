from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        queue = deque()
        for i, num in enumerate(nums):
            while queue and i - queue[0] >= k:
                queue.popleft()

            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
