class Solution:
    def inorderTraversal(self, root):
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return []

