class Codec:
    def deserialize(self, data):
        def buildTree(preorder):
            value = preorder.pop(0)
            if value == '#':
                return None
            node = TreeNode(int(value))
            node.left = buildTree(preorder)
            node.right = buildTree(preorder)
            return node
        preorder = data.split(',')[:-1]
        return buildTree(preorder)

