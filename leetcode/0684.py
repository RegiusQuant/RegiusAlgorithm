from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.hasCycle = False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(u: int, f: int):
            visit[u] = True
            for v in graph[u]:
                if v == f:
                    continue
                if not visit.get(v, False):
                    dfs(v, u)
                else:
                    self.hasCycle = True

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            self.hasCycle = False
            visit = {}
            dfs(u, 0)
            if self.hasCycle:
                return [u, v]
