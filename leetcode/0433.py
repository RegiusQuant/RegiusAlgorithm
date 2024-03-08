from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        table = {}
        queue = deque([startGene])
        table[startGene] = 0
        while queue:
            s = queue.popleft()
            for i in range(8):
                for c in "ACGT":
                    if s[i] == c:
                        continue
                    t = s[: i] + c + s[i + 1:]
                    if t in bank and t not in table:
                        table[t] = table[s] + 1
                        queue.append(t)

        return table.get(endGene, -1)
