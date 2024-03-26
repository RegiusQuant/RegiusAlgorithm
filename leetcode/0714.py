from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        table = defaultdict(lambda: float("-inf"))
        table[(0, 0)] = 0
        table[(0, 1)] = -prices[0]

        for i in range(1, len(prices)):
            table[(i, 0)] = max(table[(i - 1, 0)], table[(i - 1, 1)] + prices[i] - fee)
            table[(i, 1)] = max(table[(i - 1, 1)], table[(i - 1, 0)] - prices[i])

        return max(table.values())
