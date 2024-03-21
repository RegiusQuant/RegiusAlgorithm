from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if self.check(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, weights: List[int], days: int, val: int) -> bool:
        total, curr = 1, 0
        for weight in weights:
            if curr + weight > val:
                curr = weight
                total += 1
            else:
                curr += weight
        return total <= days
