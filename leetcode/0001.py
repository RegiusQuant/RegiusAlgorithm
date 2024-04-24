from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[num] = i
        return []
