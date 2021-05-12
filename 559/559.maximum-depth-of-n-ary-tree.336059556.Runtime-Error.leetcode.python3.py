class Solution(object):
    def maxDepth(self, root):
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)

