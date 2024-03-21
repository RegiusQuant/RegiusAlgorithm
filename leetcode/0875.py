import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.check(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, piles: List[int], h: int, val: int) -> bool:
        total = 0
        for p in piles:
            total += math.ceil(p / val)
        return total <= h
