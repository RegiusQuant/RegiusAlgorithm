from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(1, len(nums)):
            total = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    total = count[j]
                elif dp[j] + 1 == dp[i]:
                    total += count[j]
            count[i] = total

        result, maxLength = 1, 0
        for i in range(len(nums)):
            if dp[i] > maxLength:
                maxLength = dp[i]
                result = count[i]
            elif dp[i] == maxLength:
                result += count[i]
        return result
