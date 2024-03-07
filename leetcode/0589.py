from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(root: 'Node'):
            if not root:
                return

            result.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return result
