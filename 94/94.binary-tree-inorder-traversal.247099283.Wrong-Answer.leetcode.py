class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return
        result = []
        self.inorderTraversal(root.left)
        result.append(root.val)
        self.inorderTraversal(root.right)
        return result

