class Solution(object):
    def invertTree(self, root):
        if not root:
            return
        leftTree = self.invertTree(root.left)
        rightTree = self.invertTree(root.right)
        root.left = rightTree
        root.right = leftTree
        return root

