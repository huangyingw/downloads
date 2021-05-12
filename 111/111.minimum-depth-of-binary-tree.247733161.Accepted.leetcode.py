class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left or not right:
            return 1 + left + right
        return 1 + min(left, right)

