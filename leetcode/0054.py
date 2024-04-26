from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        m, n = len(matrix), len(matrix[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = [[False] * n for _ in range(m)]
        currRow, currCol, currIndex = 0, 0, 0

        for _ in range(m * n):
            result.append(matrix[currRow][currCol])
            visited[currRow][currCol] = True

            nextRow, nextCol = currRow + directions[currIndex][0], currCol + directions[currIndex][1]
            if not (0 <= nextRow < m and 0 <= nextCol < n and not visited[nextRow][nextCol]):
                currIndex = (currIndex + 1) % 4
            currRow, currCol = currRow + directions[currIndex][0], currCol + directions[currIndex][1]

        return result
