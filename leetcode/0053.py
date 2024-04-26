from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)

        currSum = 0
        for num in nums:
            currSum = max(0, currSum) + num
            result = max(result, currSum)

        return result
