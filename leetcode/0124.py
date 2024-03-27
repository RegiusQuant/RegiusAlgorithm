from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.result = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.result = max(self.result, left + right + node.val)

            return node.val + max(left, right)

        dfs(root)
        return self.result
