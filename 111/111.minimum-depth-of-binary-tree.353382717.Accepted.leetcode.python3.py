class Solution(object):
    def minDepth(self, root, hasBrother=False):
        print('def minDepth --> ');
        if not root:
            return float("inf") if hasBrother else 0
        return min(self.minDepth(root.left, root.right), self.minDepth(root.right, root.left)) + 1

