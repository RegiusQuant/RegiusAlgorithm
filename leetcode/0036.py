from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                t = board[i][j]

                if t in row[i]:
                    return False
                row[i].add(t)

                if t in col[j]:
                    return False
                col[j].add(t)

                k = i // 3 * 3 + j // 3
                if t in box[k]:
                    return False
                box[k].add(t)

        return True
