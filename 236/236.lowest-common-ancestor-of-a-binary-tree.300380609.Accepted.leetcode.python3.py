class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca and right_lca:
            return root
        return left_lca or right_lca

