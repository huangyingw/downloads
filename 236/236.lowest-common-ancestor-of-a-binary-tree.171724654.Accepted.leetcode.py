class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left if left else right

