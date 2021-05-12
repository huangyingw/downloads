class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left:
            return right + 1
        if not root.right:
            return left + 1
        return min(left, right) + 1

