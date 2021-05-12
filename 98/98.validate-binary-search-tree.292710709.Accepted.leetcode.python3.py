class Solution(object):
    def isValidBST(self, root):
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, node, lower, upper):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return self.valid(node.left, lower, node.val) and self.valid(node.right, node.val, upper)

