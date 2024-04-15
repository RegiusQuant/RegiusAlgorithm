from typing import List


class DisjointSet:

    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.root[x] = y
            return True
        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((w, i, j))
        edges.sort()

        result, count = 0, 0
        s = DisjointSet(n)
        for w, u, v in edges:
            if s.union(u, v):
                result += w
                count += 1
                if count == n - 1:
                    break
        return result
