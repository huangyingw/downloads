class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return root if not left else left

