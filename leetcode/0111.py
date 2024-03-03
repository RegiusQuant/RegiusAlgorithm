from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.calculate(root, 1)

    def calculate(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return depth

        if root.left and root.right:
            return min(self.calculate(root.left, depth + 1), self.calculate(root.right, depth + 1))
        elif root.left:
            return self.calculate(root.left, depth + 1)
        else:
            return self.calculate(root.right, depth + 1)
