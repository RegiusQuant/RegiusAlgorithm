from functools import cache
from typing import List


class Solution:
    @cache
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        result = []
        for k in range(1, n + 1):
            A = self.generateParenthesis(k - 1)
            B = self.generateParenthesis(n - k)

            for a in A:
                for b in B:
                    result.append(f"({a}){b}")
        return result
