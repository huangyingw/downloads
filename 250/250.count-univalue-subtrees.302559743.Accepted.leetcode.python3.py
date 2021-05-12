class Solution():
    def countUnivalSubtrees(self, root):
        self.univariates = 0
        self.preorder(root)
        return self.univariates

    def preorder(self, root):
        if not root:
            return
        if self.is_univariate(root):
            self.univariates += 1
        self.preorder(root.left)
        self.preorder(root.right)

    def is_univariate(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.is_univariate(root.left) and self.is_univariate(root.right)

