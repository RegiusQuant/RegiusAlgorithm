from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        table = {}
        for i, num in enumerate(nums):
            if num not in table:
                table[num] = [1, i, i]
            else:
                table[num][0] += 1
                table[num][2] = i

        maxCount, minLength = 0, 0
        for count, left, right in table.values():
            if count > maxCount:
                maxCount = count
                minLength = right - left + 1
            elif count == maxCount:
                minLength = min(minLength, right - left + 1)

        return minLength
