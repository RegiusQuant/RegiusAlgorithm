from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set([0])
        for i in range(len(nums)):
            for v in sorted(dp, reverse=True):
                dp.add(v + nums[i])

        return sum(nums) // 2 in dp
