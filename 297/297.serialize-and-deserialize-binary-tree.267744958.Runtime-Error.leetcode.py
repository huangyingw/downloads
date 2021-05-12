class Codec:
    def serialize(self, root):
        def preorder(root):
            if root:
                seralizeTree.append(str(root.val) + ',')
                preorder(root.left)
                preorder(root.right)
            else:
                seralizeTree.append('#,')
        seralizeTree = []
        preorder(root)
        return ''.join(seralizeTree)

