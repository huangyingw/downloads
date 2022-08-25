class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        return self.getDepth(root) >= 0

    def getDepth(self, node):
        if not node:
            return 1
        ld = self.getDepth(node.left)
        if ld < 0:
            return -1
        rd = self.getDepth(node.right)
        if rd < 0:
            return -1
        elif abs(ld - rd) > 1:
            return -1
        else:
            return max(ld, rd) + 1

