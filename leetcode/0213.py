from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = 0

        table = [[0] * 2 for _ in range(len(nums))]
        table[0][0] = 0
        table[0][1] = float("-inf")

        for i in range(1, len(nums)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1])
            table[i][1] = table[i - 1][0] + nums[i]

        result = max(result, max(table[-1]))

        table[0][0] = 0
        table[0][1] = nums[0]

        for i in range(1, len(nums)):
            table[i][0] = max(table[i - 1][0], table[i - 1][1])
            table[i][1] = table[i - 1][0] + nums[i]

        result = max(result, table[-1][0])
        return result
