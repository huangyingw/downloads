class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val > q.val:
                root = root.left
            else:
                return root

