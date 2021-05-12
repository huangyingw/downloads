class Solution:
    def preorderTraversal(self, root):
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return []

