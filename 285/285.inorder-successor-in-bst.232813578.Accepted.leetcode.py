class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            # think in this way: find the smallest element
            # that is larger than p
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

