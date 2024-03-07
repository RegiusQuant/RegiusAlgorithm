from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if depth > len(result):
                result.append([])
            result[-1].append(node.val)
            for child in node.children:
                queue.append((child, depth + 1))
        return result
