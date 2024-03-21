from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.check(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, nums: List[int], k: int, val: int) -> bool:
        total, curr = 1, 0
        for num in nums:
            if curr + num > val:
                total += 1
                curr = num
            else:
                curr += num
        return total <= k
