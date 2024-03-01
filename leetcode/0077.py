from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def search(depth: int, chosen: List[int]):
            if depth == n:
                if len(chosen) == k:
                    result.append(chosen)
                return

            search(depth + 1, chosen)
            search(depth + 1, chosen + [depth + 1])

        search(0, [])
        return result
