from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)
            degree[v] += 1

        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)

        lessons = []
        while queue:
            u = queue.popleft()
            lessons.append(u)
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)

        if len(lessons) != numCourses:
            return []
        return lessons
