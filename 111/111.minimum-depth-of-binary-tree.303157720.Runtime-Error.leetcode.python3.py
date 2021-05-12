class Solution(object):
    def minDepth(self, root, hasBrother=False):
        if not root:
            return sys.maxint if hasBrother else 0
        return min(self.minDepth(root.left, root.right), self.minDepth(root.right, root.left)) + 1

