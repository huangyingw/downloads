class Solution:
    def postorderTraversal(self, root):
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return []

