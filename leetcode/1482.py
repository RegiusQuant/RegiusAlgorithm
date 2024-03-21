from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.check(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def check(self, bloomDay: List[int], m: int, k: int, val: int) -> bool:
        total, count = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= val:
                count += 1
                if count == k:
                    count = 0
                    total += 1
            else:
                count = 0
        return total >= m
