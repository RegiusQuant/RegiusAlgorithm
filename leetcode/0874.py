from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        s = set()
        for obstacle in obstacles:
            s.add(tuple(obstacle))

        result = 0
        x, y, d = 0, 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d + 3) % 4
            else:
                for _ in range(command):
                    nx, ny = x + directions[d][0], y + directions[d][1]
                    if (nx, ny) in s:
                        break
                    x, y = nx, ny
                    result = max(result, x ** 2 + y ** 2)

        return result
