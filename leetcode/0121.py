from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        minValue = prices[0]
        for price in prices[1:]:
            result = max(result, price - minValue)
            minValue = min(minValue, price)

        return result
