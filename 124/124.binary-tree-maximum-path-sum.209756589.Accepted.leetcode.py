class Solution(object):
    def __init__(self):
        self.max = -sys.maxint - 1

    def maxPathSum(self, root):
        self.findMax(root)
        return self.max

    def findMax(self, root):
        if not root:
            return 0

        left = max(self.findMax(root.left), 0)
        right = max(self.findMax(root.right), 0)
        self.max = max(self.max, root.val + left + right)
        return root.val + max(left, right)

