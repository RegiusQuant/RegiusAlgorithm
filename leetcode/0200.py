from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = [[False] * n for _ in range(m)]
        dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]
        queue = deque()

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0" or visit[i][j]:
                    continue
                
                result += 1
                queue.append((i, j))
                visit[i][j] = True
                while queue:
                    cx, cy = queue.popleft()
                    for k in range(4):
                        nx ,ny = cx + dx[k], cy + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and grid[nx][ny] != "0":
                            queue.append((nx, ny))
                            visit[nx][ny] = True

        return result
