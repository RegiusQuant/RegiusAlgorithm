from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        result = -1
        minCities = n + 1
        for i in range(n):
            temp = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    temp += 1
            if temp <= minCities:
                minCities = temp
                result = i
        return result
