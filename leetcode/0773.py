from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start, target = self.encodeBoard(board), "123450"
        queue = deque([start])
        depth = {start: 0}

        def expandState(s: str, pos: int, other: int):
            t = list(s)
            t[pos], t[other] = t[other], t[pos]
            t = "".join(t)

            if t in depth:
                return
            depth[t] = depth[s] + 1
            queue.append(t)

        while queue:
            s = queue.popleft()
            pos = s.index("0")

            if pos >= 3:
                expandState(s, pos, pos - 3)
            if pos <= 2:
                expandState(s, pos, pos + 3)
            if pos % 3 > 0:
                expandState(s, pos, pos - 1)
            if pos % 3 < 2:
                expandState(s, pos, pos + 1)

            if target in depth:
                return depth[target]

        return -1

    def encodeBoard(self, board: List[List[int]]) -> str:
        key = ""
        for i in range(2):
            for j in range(3):
                key += str(board[i][j])
        return key
