from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = defaultdict(lambda: float("-inf"))
        table[(0, 0, 0)] = 0
        table[(0, 1, 0)] = -prices[0]

        for i in range(1, len(prices)):
            for j in [0, 1]:
                for k in [0, 1, 2]:
                    table[(i, j, k)] = table[(i - 1, j, k)]

            for k in [0, 1]:
                table[(i, 1, k)] = max(table[(i, 1, k)], table[(i - 1, 0, k)] - prices[i])
            for k in [1, 2]:
                table[(i, 0, k)] = max(table[(i, 0, k)], table[(i - 1, 1, k - 1)] + prices[i])

        return max(table.values())
