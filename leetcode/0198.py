from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [[0] * 2 for _ in range(len(nums))]
        table[0][0] = 0
        table[0][1] = nums[0]

        for i in range(1, len(nums)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1])
            table[i][1] = table[i - 1][0] + nums[i]

        return max(table[-1])
