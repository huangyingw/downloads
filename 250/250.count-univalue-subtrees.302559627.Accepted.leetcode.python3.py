class Solution(object):
    def countUnivalSubtrees(self, root):
        self.univariates = 0
        self.is_univariate(root)
        return self.univariates

    def is_univariate(self, root):
        if not root:
            return True
        left_uni = self.is_univariate(root.left)
        right_uni = self.is_univariate(root.right)
        if left_uni and right_uni:
            if (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                self.univariates += 1
                return True
        return False

