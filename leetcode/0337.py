from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0, 0

            l0, l1 = dfs(node.left)
            r0, r1 = dfs(node.right)
            return max(l0, l1) + max(r0, r1), l0 + r0 + node.val

        return max(dfs(root))
