from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        dfs(root)
        return result
