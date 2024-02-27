from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, x in enumerate(nums):
            if (target - x) in table:
                return [table[target - x], i]
            table[x] = i
