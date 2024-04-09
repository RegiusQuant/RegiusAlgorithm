from typing import List


class DisjointSet:

    def __init__(self, n: int):
        self.root = [x for x in range(n)]

    def find(self, x: int):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def merge(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[x] = y


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        ds = DisjointSet(m * n + 1)

        def code(x: int, y: int) -> int:
            nonlocal m, n
            return x * n + y

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        ds.merge(code(i, j), m * n)
                    elif board[nx][ny] == "O":
                        ds.merge(code(i, j), code(nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and ds.find(code(i, j)) != ds.find(m * n):
                    board[i][j] = "X"
