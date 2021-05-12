class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root:
            return root
        flippedRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return flippedRoot

