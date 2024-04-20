from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                t = int(board[i][j]) - 1
                row[i].add(t)
                col[j].add(t)
                k = i // 3 * 3 + j // 3
                box[k].add(t)

        def dfs(x: int, y: int):
            if y == 9:
                x, y = x + 1, 0
            if x == 9:
                return True

            if board[x][y] != ".":
                return dfs(x, y + 1)

            k = x // 3 * 3 + y // 3
            for t in range(9):
                if t in row[x] or t in col[y] or t in box[k]:
                    continue
                board[x][y] = str(t + 1)
                row[x].add(t)
                col[y].add(t)
                box[k].add(t)
                if dfs(x, y + 1):
                    return True
                board[x][y] = "."
                row[x].remove(t)
                col[y].remove(t)
                box[k].remove(t)

        dfs(0, 0)
