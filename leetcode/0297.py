class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.curr = 0

    def serialize(self, root):
        data = []

        def dfs(root: TreeNode):
            if root is None:
                data.append("null")
                return
            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(data)

    def deserialize(self, data):
        data = data.split(",")
        self.curr = 0

        def restore():
            if data[self.curr] == "null":
                self.curr += 1
                return None

            node = TreeNode(int(data[self.curr]))
            self.curr += 1
            node.left = restore()
            node.right = restore()
            return node

        return restore()
