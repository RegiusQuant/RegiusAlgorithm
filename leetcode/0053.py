from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")

        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        prefixMin = [0]
        for i in range(1, len(prefixSum)):
            prefixMin.append(min(prefixMin[i - 1], prefixSum[i]))

        for i in range(1, len(prefixSum)):
            result = max(result, prefixSum[i] - prefixMin[i - 1])

        return result
