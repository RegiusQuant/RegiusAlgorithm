from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        table = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        result = []

        def dfs(depth: int, s: str):
            if depth == len(digits):
                result.append(s)
                return
            for c in table[digits[depth]]:
                dfs(depth + 1, s + c)

        dfs(0, "")
        return result
