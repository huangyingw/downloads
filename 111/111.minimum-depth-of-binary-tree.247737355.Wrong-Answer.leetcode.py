class Solution(object):
    def minDepth(self, root):
        def minDepth(root, hasBrother):
            if not root:
                return sys.maxint if hasBrother else 0
            return min(minDepth(root.left, root.right), minDepth(root.right, root.left))
        return minDepth(root, False)

