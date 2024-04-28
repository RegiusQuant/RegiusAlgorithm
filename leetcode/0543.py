from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxNodes = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            nonlocal maxNodes
            leftDepth, rigfhtDepth = dfs(node.left), dfs(node.right)
            maxNodes = max(maxNodes, leftDepth + rigfhtDepth + 1)
            return max(leftDepth, rigfhtDepth) + 1

        dfs(root)
        return maxNodes - 1
