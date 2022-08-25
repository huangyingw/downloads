class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        flag = abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        return flag and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

