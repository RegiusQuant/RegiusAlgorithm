from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        table = defaultdict(lambda: float("-inf"))
        table[(0, 0, 0)] = 0
        table[(0, 1, 0)] = -prices[0]

        for i in range(1, len(prices)):
            for j in [0, 1]:
                for c in range(k + 1):
                    table[(i, j, c)] = table[(i - 1, j, c)]

            for c in range(k + 1):
                if c != k:
                    table[(i, 1, c)] = max(table[(i, 1, c)], table[(i - 1, 0, c)] - prices[i])
                if c != 0:
                    table[(i, 0, c)] = max(table[(i, 0, c)], table[(i - 1, 1, c - 1)] + prices[i])

        return max(table.values())
