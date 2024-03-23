from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        maxPos, end, step = 0, 0, 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
        return step
