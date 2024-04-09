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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ds.merge(i, j)

        result = 0
        for i in range(n):
            if ds.root[i] == i:
                result += 1
        return result
