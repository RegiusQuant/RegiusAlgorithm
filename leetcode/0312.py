from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        @lru_cache(None)
        def solve(left: int, right: int):
            if left > right:
                return 0

            result = 0
            for p in range(left, right + 1):
                temp = solve(left, p - 1) + solve(p + 1, right) + nums[left - 1] * nums[p] * nums[right + 1]
                result = max(result, temp)
            return result

        return solve(1, n)
