from collections import Counter
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        prefixSum, table = 0, Counter([0])
        for num in nums:
            prefixSum += num
            result += table[prefixSum - k]
            table[prefixSum] += 1

        return result
