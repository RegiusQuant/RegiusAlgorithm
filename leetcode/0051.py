from collections import defaultdict
from copy import deepcopy
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        usedCol, usedAdd, usedSub = defaultdict(bool), defaultdict(bool), defaultdict(bool)
        result, position = [], []

        def dfs(row: int):
            if row == n:
                result.append(deepcopy(position))
                return

            for col in range(n):
                if usedCol[col] or usedAdd[row + col] or usedSub[row - col]:
                    continue

                position.append(col)
                usedCol[col] = usedAdd[row + col] = usedSub[row - col] = True

                dfs(row + 1)

                position.pop()
                usedCol[col] = usedAdd[row + col] = usedSub[row - col] = False

        dfs(0)

        for r in result:
            for i, c in enumerate(r):
                temp = ["."] * n
                temp[c] = "Q"
                r[i] = "".join(temp)

        return result
