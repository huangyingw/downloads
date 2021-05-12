class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if max(p.val, p.val) < root.val:
                root = root.left
            elif min(p.val, p.val) > root.val:
                root = root.right
            else:
                return root

