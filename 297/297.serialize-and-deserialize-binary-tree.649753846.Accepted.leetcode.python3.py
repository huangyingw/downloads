class Codec:
    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        vals = []
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        def preorder():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        vals = iter(data.split())
        return preorder()

