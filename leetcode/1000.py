from functools import cache
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if k != 2 and len(stones) % (k - 1) != 1:
            return -1

        @cache
        def solve(left: int, right: int, c: int) -> int:
            nonlocal k

            if c == 1:
                if left == right:
                    return 0
                else:
                    return solve(left, right, k) + sum(stones[left: right + 1])

            result = float("inf")
            for p in range(left, right, k - 1):
                result = min(result, solve(left, p, 1) + solve(p + 1, right, c - 1))
            return result

        return solve(0, len(stones) - 1, 1)
