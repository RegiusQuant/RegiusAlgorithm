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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = DisjointSet(n + 1)

        for u, v in edges:
            if ds.find(u) == ds.find(v):
                return [u, v]
            ds.merge(u, v)
