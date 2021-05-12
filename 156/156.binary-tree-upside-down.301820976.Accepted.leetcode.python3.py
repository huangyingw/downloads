class Solution(object):
    def upsideDownBinaryTree(self, root):
        if root is None:
            return root
        if not root.left and not root.right:
            return root
        flippedRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return flippedRoot

