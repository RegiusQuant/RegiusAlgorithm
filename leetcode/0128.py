from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, table = 0, {}
        
        for num in set(nums):
            if num in table:
                continue
            
            left, right = table.get(num - 1, 0), table.get(num + 1, 0)
            length = left + right + 1
            table[num - left] = table[num + right] = length
            result = max(result, length)

        return result
