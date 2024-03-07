class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode'):
            if not root:
                return False, False

            left, right = dfs(root.left), dfs(root.right)
            findP = left[0] or right[0] or root.val == p.val
            findQ = left[1] or right[1] or root.val == q.val
            if findP and findQ and self.result is None:
                self.result = root

            return findP, findQ

        dfs(root)
        return self.result
