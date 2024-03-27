from collections import deque
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums + nums

        s = [0]
        for i in range(1, len(nums)):
            s.append(s[-1] + nums[i])

        result = float("-inf")
        queue = deque([(0, 0)])
        for i in range(1, len(nums)):
            while queue and i - queue[0][0] > n:
                queue.popleft()
            result = max(result, s[i] - queue[0][1])
            while queue and s[i] < queue[-1][1]:
                queue.pop()
            queue.append((i, s[i]))

        return result
