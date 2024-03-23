from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax = [0] * len(nums)
        fmin = [0] * len(nums)
        fmax[0] = fmin[0] = nums[0]

        for i in range(1, len(nums)):
            fmax[i] = max(fmax[i - 1] * nums[i], fmin[i - 1] * nums[i], nums[i])
            fmin[i] = min(fmax[i - 1] * nums[i], fmin[i - 1] * nums[i], nums[i])

        return max(fmax)
