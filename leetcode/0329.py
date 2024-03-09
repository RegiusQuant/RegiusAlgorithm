from collections import defaultdict, deque, Counter
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
        graph = defaultdict(list)
        degree = Counter()

        for cx in range(m):
            for cy in range(n):
                for k in range(4):
                    nx, ny = cx + dx[k], cy + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[cx][cy]:
                        graph[(cx, cy)].append((nx, ny))
                        degree[(nx, ny)] += 1

        queue = deque()
        dist = {}
        for cx in range(m):
            for cy in range(n):
                if degree[(cx, cy)] == 0:
                    queue.append((cx, cy))
                    dist[(cx, cy)] = 1

        while queue:
            cx, cy = queue.popleft()
            for nx, ny in graph[(cx, cy)]:
                degree[(nx, ny)] -= 1
                dist[(nx, ny)] = max(dist.get((nx, ny), 0), dist[(cx, cy)] + 1)
                if degree[(nx, ny)] == 0:
                    queue.append((nx, ny))

        return max(dist.values())
