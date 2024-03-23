from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if i != 0:
                        dp[i][j] += dp[i - 1][j]
                    if j != 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[n - 1][m - 1]
