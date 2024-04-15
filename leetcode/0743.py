from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        queue = deque()
        visit = [False] * (n + 1)
        dist = [float("inf")] * (n + 1)

        queue.append(k)
        visit[k] = True
        dist[k] = 0

        while queue:
            u = queue.popleft()
            visit[u] = False

            for v, w in edges[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if not visit[v]:
                        queue.append(v)
                        visit[v] = True

        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1
