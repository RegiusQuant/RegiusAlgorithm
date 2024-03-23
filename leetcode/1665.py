from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1], reverse=True)

        result = 0
        for task in tasks:
            result = max(result + task[0], task[1])
        return result
