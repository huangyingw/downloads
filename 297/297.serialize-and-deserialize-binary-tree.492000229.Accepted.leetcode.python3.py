

class Codec:

    def serialize(self, root):

        if not root:
            return None
        res = root.val
        a = self.serialize(root.left)
        b = self.serialize(root.right)
        return f"{res},{a},{b}"

    def deserialize(self, data):

        if not data:
            return

        def helper(data):
            if not data:
                return

            d = data.pop(0)
            if d == "None":
                return

            root = TreeNode(d)
            root.left = helper(data)
            root.right = helper(data)
            return root

        return helper(data.split(","))

