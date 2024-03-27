from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        result = float("-inf")

        queue = deque([(points[0][1] - points[0][0], points[0][0])])
        for i in range(1, len(points)):
            while queue and points[i][0] - queue[0][1] > k:
                queue.popleft()

            if queue:
                result = max(result, points[i][0] + points[i][1] + queue[0][0])

            while queue and points[i][1] - points[i][0] >= queue[-1][0]:
                queue.pop()
            queue.append((points[i][1] - points[i][0], points[i][0]))

        return result
